from django.urls import path
from .views import user_account_create, user_account_list

urlpatterns = [
    path('create/', user_account_create, name='user_account_create'),
    path('list/', user_account_list, name='user_account_list'),
]
