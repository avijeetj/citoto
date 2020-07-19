from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('home/', home, name='signup'),
    path('validate-otp/', validate_otp, name='otp_validation'),
]