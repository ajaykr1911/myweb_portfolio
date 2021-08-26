from os import name
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('projects/', views.projects, name='ML'),
    path('projects/', views.projects, name='web'),
    path('cv/', views.cv, name='cv')
]
