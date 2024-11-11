from django.shortcuts import render, redirect
from .forms import UserDataForm
from .models import UserData

def user_data_create(request):
    if request.method == 'POST':
        form = UserDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_data_list')
    else:
        form = UserDataForm()
    return render(request, 'user_account/user_data_form.html', {'form': form})

def user_data_list(request):
    data = UserData.objects.all().order_by('-submission_date')
    return render(request, 'user_account/user_data_list.html', {'data': data})
