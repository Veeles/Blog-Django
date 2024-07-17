from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static 
from django.http import HttpResponse
from django.urls import path
from . import views
import os

urlpatterns = [
    path('register/', views.register, name='register'),

] 

