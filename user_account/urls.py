from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                     # Home page
    path('new/', views.user_data_create, name='user_data_create'),  # Form for new data entry
    path('list/', views.user_data_list, name='user_data_list'),     # List of entries
]
