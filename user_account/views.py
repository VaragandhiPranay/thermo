from django.shortcuts import render, redirect
from .forms import UserAccountForm
from .models import UserAccount

def user_account_create(request):
    if request.method == "POST":
        form = UserAccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_account_list')
    else:
        form = UserAccountForm()
    return render(request, 'user_account/user_account_form.html', {'form': form})

def user_account_list(request):
    user_accounts = UserAccount.objects.all().order_by('submission_date')
    return render(request, 'user_account/user_account_list.html', {'user_accounts': user_accounts})
