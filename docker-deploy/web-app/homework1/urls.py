"""homework1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from users import views as user_views
from ride import views as ride_views

urlpatterns = [
    path('',user_views.login,name='login'),
    path('admin/', admin.site.urls),
    path('register/',user_views.register,name='register'),
    path('profile/',user_views.profile,name='profile'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('loginerror/',user_views.loginerror,name='loginerror'),
    path('d_error/',user_views.d_error,name='d_error'),
    path('d_info/',user_views.d_info,name='d_info'),
    
    path('status/', ride_views.view_all_status, name='status'),
    path('d_status/', ride_views.driver_status, name='d_status'),
    path('edit_ride/<int:rideNumber>/', ride_views.edit_ride, name='edit_ride'),
    path('delete_ride/<int:rideNumber>/', ride_views.delete_ride, name='delete_ride'),
    path('look_for_shared_ride/', ride_views.look_for_shared_ride, name='look_for_shared_ride'),
    path('join_ride/<int:rideNumber>/', ride_views.join_ride, name='join_ride'),
    path('look_for_open_ride/', ride_views.look_for_open_ride, name='look_for_open_ride'),
    path('claim_ride/<int:rideNumber>/', ride_views.claim_ride, name='claim_ride'),
    path('complete_ride/<int:rideNumber>/', ride_views.complete_ride, name='complete_ride'),
]
