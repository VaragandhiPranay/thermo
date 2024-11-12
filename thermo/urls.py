from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_account.urls')),  # Redirect root to user account app, with home as default
]
