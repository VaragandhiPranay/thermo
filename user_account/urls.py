# D:\Projects\Project4_thermo\thermo\user_account\urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.user_data_create, name='user_data_create'),  # Form to create user data
    path('list/', views.user_data_list, name='user_data_list'),     # Display user data list
]
