from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                     # Home page
    path('new/', views.user_data_create, name='user_data_create'),  # Create view
    path('list/', views.user_data_list, name='user_data_list'),     # List view
    path('edit/<int:pk>/', views.user_data_update, name='user_data_update'),  # Update view
    path('delete/<int:pk>/', views.user_data_delete, name='user_data_delete'), # Delete view
    path('api/userdata/<int:pk>/', views.UserDataDetail.as_view(), name='user_data_detail'),  # API endpoint for CRUD
]
