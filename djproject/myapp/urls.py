# This file was created anew

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')   # second parameter calls 'index' function from views.py
]