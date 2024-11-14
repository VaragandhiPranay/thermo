# views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .forms import UserDataForm
from .models import UserData
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserDataSerializer

# Home View
def home(request):
    return render(request, 'user_account/home.html')

# Create View
def user_data_create(request):
    if request.method == 'POST':
        form = UserDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_data_list')
    else:
        form = UserDataForm()
    return render(request, 'user_account/user_data_form.html', {'form': form})

# List View with Search
# views.py
def user_data_list(request):
    query = request.GET.get('search', '').strip()
    sort_by = request.GET.get('sort_by', 'submission_date')  # Default sorting field
    order = request.GET.get('order', 'desc')  # Default order is descending

    # Determine sorting order
    if order == 'desc':
        sort_by = f'-{sort_by}'

    # Filter data based on search query
    data = UserData.objects.filter(
        Q(name__icontains=query) | 
        Q(user_id__icontains=query) | 
        Q(email__icontains=query) | 
        Q(role__icontains=query) |
        Q(catalog_tasks_id__icontains=query)
    ).order_by(sort_by)

    # Pass sorting details to template
    return render(request, 'user_account/user_data_list.html', {
        'data': data,
        'query': query,
        'sort_by': sort_by.lstrip('-'),  # Send sort field without '-' prefix for display
        'order': order,
    })


# Update View
def user_data_update(request, pk):
    user_data = get_object_or_404(UserData, pk=pk)
    if request.method == 'POST':
        form = UserDataForm(request.POST, instance=user_data)
        if form.is_valid():
            form.save()
            return redirect('user_data_list')
    else:
        form = UserDataForm(instance=user_data)
    return render(request, 'user_account/user_data_form.html', {'form': form})

# Delete View
def user_data_delete(request, pk):
    user_data = get_object_or_404(UserData, pk=pk)
    if request.method == 'POST':
        user_data.delete()
        return redirect('user_data_list')
    return render(request, 'user_account/user_data_confirm_delete.html', {'user_data': user_data})

# API Detail View for CRUD operations using DRF
class UserDataDetail(APIView):
    def get(self, request, pk):
        user_data = get_object_or_404(UserData, pk=pk)
        serializer = UserDataSerializer(user_data)
        return Response(serializer.data)

    def put(self, request, pk):
        user_data = get_object_or_404(UserData, pk=pk)
        serializer = UserDataSerializer(user_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        user_data = get_object_or_404(UserData, pk=pk)
        serializer = UserDataSerializer(user_data, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user_data = get_object_or_404(UserData, pk=pk)
        user_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


import csv
from django.http import HttpResponse
from .models import UserData

import csv
from django.http import HttpResponse
from .models import UserData

def export_user_data_pipe_separated(request):
    users = UserData.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="user_data.txt"'

    writer = csv.writer(response, delimiter='|')  # Use '|' as the delimiter

    for user in users:
        writer.writerow([
            user.name,
            user.user_id,
            '',  # Empty field as requested
            user.group,
            user.role,
            'licenselevel',  # Static text as requested
            'author' if user.role == 'Designer' else 'consumer',  # 'author' for Designer role, else 'consumer'
            'status',  # Static text as requested
            '0',  # Static text as requested
            'PA6',  # Static text as requested
            user.employment_type,  # Will contain either "MSD" or the company name directly
            'PA9',  # Static text as requested
            user.email,
            'ip_clearance',  # Static text as requested
            user.ip_clearance_status if user.ip_clearance_status is not None else ''  # Leave blank if null
        ])

    return response

