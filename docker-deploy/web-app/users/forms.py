from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MaxValueValidator, MinValueValidator
from .models import Profile


class UserRegisterForm(UserCreationForm):
  email = forms.EmailField()
  first_name = forms.CharField(max_length=100)
  last_name = forms.CharField(max_length=100)
  class Meta:
    model = User
    fields = ['username', 'email','first_name','last_name','password1', 'password2']
    
class UserUpdate(forms.ModelForm):
  email = forms.EmailField()
  first_name = forms.CharField(max_length=100)
  last_name = forms.CharField(max_length=100)
  class Meta:
    model = User
    fields = ['username', 'email','first_name','last_name']

    
class DriverRegisterForm(forms.ModelForm):
  isdriver = forms.BooleanField(label='Do you want to be a driver?', required=False)
  license = forms.CharField(label='Driver License*', max_length=100,required=False)
  vehicle_type = forms.ChoiceField(label='Vehicle Type',
                              choices=( ("Sedan", "Sedan"),
                                        ("SUV", "SUV")),required=False)
  pnum = forms.IntegerField(label='Maximum Number of Passengers', required=False, validators=[MinValueValidator(1), MaxValueValidator(7)])
  child = forms.BooleanField(label='Child Seat(optional)', required=False)
  
  class Meta:
    model = Profile
    fields = ['isdriver','license','vehicle_type','pnum','child']
    
    
     
    
    
class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    isdriver = forms.BooleanField(label='Are you a driver?', required=False)
    
    class Meta:
      model = User
      fields = ['username', 'password','isdriver']