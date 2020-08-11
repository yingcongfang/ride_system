from django.shortcuts import render,redirect

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from django.contrib import messages, auth
from .forms import UserRegisterForm, LoginForm,DriverRegisterForm,UserUpdate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

def loginerror(request):
  return render(request,'users/loginerror.html')

def d_error(request):
  return render(request,'users/d_error.html')

def register(request):
  if request.method == 'POST':
    form = UserRegisterForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, f'Success! You are able to log in!')
      return redirect('login')
  else:
    form = UserRegisterForm()
  return render(request, 'users/register.html',{'form':form})
  
@login_required
def profile(request):
  if request.method == 'POST':
    u_form = UserUpdate(request.POST,instance=request.user)
    
    if u_form.is_valid:
      u_form.save()
      
      messages.success(request, f'Your account has been updated')
      return redirect('status')
      
  else:
    u_form = UserUpdate(instance=request.user)

  return render(request, 'users/profile.html',{'u_form':u_form})


def d_info(request):
  if request.method == 'POST':
    p_form = DriverRegisterForm(request.POST, request.FILES, instance=request.user.profile)
    
    if p_form.is_valid():
      p_form.save()
      return redirect('status')
  else:
    p_form = DriverRegisterForm(instance=request.user.profile)
    return render(request, 'users/d_info.html',{'p_form':p_form})
      
      
      
      
    
def login(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            isdriver = form.cleaned_data['isdriver']
        
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Logged in success!')
                if isdriver and request.user.profile.isdriver:
                  return HttpResponseRedirect('/d_status/')
                elif isdriver and request.user.profile.isdriver == False:
                  #messages.error(request, 'You are not a driver yet!')
                  return HttpResponseRedirect('/d_error/')
                else:
                  return HttpResponseRedirect('/status/')
            else:
             return HttpResponseRedirect('/loginerror/')
        else:
          return HttpResponseRedirect('/loginerror/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()
        args = {'form': form}    
        
    return render(request, 'users/login.html',
            {'form': form, 'message': request.session.get('message', default=None)})
       

