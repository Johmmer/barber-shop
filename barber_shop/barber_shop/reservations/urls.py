from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),
path('new-reservation', views.reserve, name='new-reservation'),
path('google-calendar/init/', views.google_calendar_init, name='google-calendar-init'),
path('oauth2callback/', views.google_calendar_redirect, name='oauth2callback'),
path('create-event', views.create_calendar_events, name='create-event'),
]
