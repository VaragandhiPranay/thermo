# D:\Projects\Project4_thermo\thermo\thermo\urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),         # Admin panel route
    path('user/', include('user_account.urls')),  # User account app routes
]
