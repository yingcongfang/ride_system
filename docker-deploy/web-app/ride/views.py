from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.mail import send_mail
from django.conf import settings
from .forms import RequestForm, SharedForm
from .models import Ride, sharedRide
from django.contrib.auth.models import User

# Create your views here.

def view_all_status(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RequestForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            request_ride = Ride(
                        name = form.cleaned_data['name'],
                        dest = form.cleaned_data['dest'],
                        arrival = form.cleaned_data['arrival'],
                        pnum = form.cleaned_data['pnum'],
                        vtype = form.cleaned_data['vtype'],
                        child = form.cleaned_data['child'],
                        share = form.cleaned_data['share'],
                        status = 'Open',
                        isOpen = True,
                        isConfirmed = False,
                        isCompleted = False,
                        #passenger_id=request.user.id
                        )
            request_ride.save()
            request_ride.user.add(request.user)
                                
            #request.session['message'] = 'Ride Request Successful'

            # redirect to a new URL:        
            return HttpResponseRedirect('/status')

    # if a GET (or any other method) we'll create a blank form
    else:
        #request.session['message'] = 'Invalid Request'
        form = RequestForm()
        args = {'form': form}
    #view current rides
    current_rides = Ride.objects.filter(user=request.user, isOpen = True)
    confirmed_rides = Ride.objects.filter(user=request.user, isConfirmed = True)
    completed_rides = Ride.objects.filter(user=request.user, isCompleted = True)
    
    
        
    return render(request, 'ride/status.html',
            {'form': form, 'current_rides': current_rides, 'confirmed_rides': confirmed_rides, 'completed_rides':completed_rides, 
            'message': request.session.get('message', default=None)})
            
def edit_ride(request, rideNumber):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            edit_ride = Ride.objects.filter(id=rideNumber)[0]
            
            edit_ride.name = form.cleaned_data['name']
            edit_ride.dest = form.cleaned_data['dest']
            edit_ride.arrival = form.cleaned_data['arrival']
            edit_ride.pnum = form.cleaned_data['pnum']
            edit_ride.vtype = form.cleaned_data['vtype']
            edit_ride.child = form.cleaned_data['child']
            edit_ride.share = form.cleaned_data['share']
            
            edit_ride.save()
            return HttpResponseRedirect('/status')

    else:
        edit_ride = Ride.objects.filter(id=rideNumber)[0]
        form = RequestForm()
        args = {'form': form}
    return render(request, 'ride/edit_ride.html', {'form':form})

def delete_ride(request, rideNumber):
    delete_ride = Ride.objects.filter(id=rideNumber)
    delete_ride.delete()
    return HttpResponseRedirect('/status')
    
arrival_s = ''
pnum_s = 0

def look_for_shared_ride(request):
    global arrival_s, pnum_s
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
    # create a form instance and populate it with data from the request:
        form = SharedForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            shared_name = form.cleaned_data['name']
            shared_dest = form.cleaned_data['dest']
            shared_arrival = form.cleaned_data['arrival']
            shared_pnum = form.cleaned_data['pnum']

            #global arrival_s, pnum_s
            arrival_s = shared_arrival
            pnum_s = shared_pnum
            shared_ride = sharedRide(
                        name = shared_name,
                        dest = shared_dest,
                        arrival = shared_arrival,
                        pnum = shared_pnum
                        )
                             
            shared_ride.save()
            shared_ride.user.add(request.user)
    
            # redirect to a new URL:        
            return HttpResponseRedirect('/look_for_shared_ride')
    else:
        form = SharedForm()
        args = {'form': form}        
    #view available rides
          
    share_rides = Ride.objects.filter(share = True, isOpen = True)
    arrival_rides = share_rides.filter(arrival = arrival_s)
    not_own_rides = arrival_rides.exclude(user=request.user)
    available_rides = not_own_rides
    
    for ride in not_own_rides:
        if (ride.vtype == 'Sedan') and (ride.pnum + pnum_s > 4):
            available_rides = available_rides.exclude(id=ride.id)
            
        elif (ride.vtype == 'SUV') and (ride.pnum + pnum_s > 6):
            available_rides = available_rides.exclude(id=ride.id)    
    arrival_s = ''
    pnum_s = 0
    return render(request, 'ride/look_for_shared_ride.html', {'form': form, 'available_rides': available_rides})
                
    
    
    
 

def join_ride(request, rideNumber):
    shared_ride = sharedRide.objects.filter(user=request.user)[0]
    join_ride = Ride.objects.filter(id=rideNumber)[0]
    
    join_ride.name += ' and ' + shared_ride.name
    #join_ride.email += request.user.email
    join_ride.dest += ' and ' + shared_ride.dest
    #join_ride.arrival += ' and ' + arrival
    join_ride.pnum += shared_ride.pnum
    
    join_ride.save()
    join_ride.user.add(request.user)
    
    shared_ride.delete()
    
    return HttpResponseRedirect('/status')
                

def driver_status(request):
    if request.user.profile.isdriver == False:
        return HttpResponseRedirect('/d_error')
    else:
        #view available rides
        #driver = User.objects.filter()[0]
        #open_rides = Ride.objects.filter(isOpen = True)#vtype = request.user., 
        confirmed_rides = Ride.objects.filter(driver_id = request.user.id ,isConfirmed = True)
        completed_rides = Ride.objects.filter(driver_id = request.user.id ,isCompleted = True)
        return render(request, 'ride/d_status.html', {'confirmed_rides': confirmed_rides, 'completed_rides': completed_rides})     


def look_for_open_ride(request):
    if request.user.profile.child == True:
        include_own_rides = Ride.objects.filter(vtype = request.user.profile.vehicle_type, isOpen = True)
        open_rides = include_own_rides.exclude(user=request.user)
    else:    
        include_own_rides = Ride.objects.filter(vtype = request.user.profile.vehicle_type, child = request.user.profile.child, isOpen = True)
        open_rides = include_own_rides.exclude(user=request.user)

    return render(request, 'ride/look_for_open_ride.html', {'open_rides': open_rides})
    


def claim_ride(request, rideNumber):
    claim_ride = Ride.objects.filter(id=rideNumber)[0]
    claim_ride.status = 'Confirmed'
    claim_ride.isOpen = False
    claim_ride.isConfirmed = True
    claim_ride.isCompleted = False
    claim_ride.driver_id = request.user.id
    claim_ride.save()
    
     
    from_email= settings.EMAIL_HOST_USER
    
    email_list = claim_ride.name.split(' and ')
    for email in email_list:
      subject = 'Your ride is comfirmed by the driver!'
      message = 'Thank you for using RideShare\n'
      message += 'Your email: ' + email +'\n'    
      message += 'Your destination: ' + claim_ride.dest + '\n'
      message += 'Your arrival window: ' + claim_ride.arrival + '\n'
      message += 'Your driver\'s id: ' + str(claim_ride.driver_id) + '\n'
      
      to_list = [email,settings.EMAIL_HOST_USER]
      send_mail(subject,message,from_email,to_list,fail_silently=False)

    
    return HttpResponseRedirect('/d_status')   
    
def complete_ride(request, rideNumber):
    complete_ride = Ride.objects.filter(id=rideNumber)[0]
    complete_ride.status = 'Completed'
    complete_ride.isOpen = False
    complete_ride.isConfirmed = False
    complete_ride.isCompleted = True
    complete_ride.save()
    return HttpResponseRedirect('/d_status')  












