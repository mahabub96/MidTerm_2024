from django.urls import path
from .views import active_subscriptions
from django.shortcuts import render

urlpatterns = [
    path('active-subscriptions/', active_subscriptions, name='active_subscriptions'),
]
