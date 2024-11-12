from django.shortcuts import render, redirect, get_object_or_404
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

# List View
def user_data_list(request):
    data = UserData.objects.all().order_by('-submission_date')  # Fetch all data
    return render(request, 'user_account/user_data_list.html', {'data': data})

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
