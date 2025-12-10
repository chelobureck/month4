from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from users.forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout

def register_view(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'users/register.html', context={'form': form})
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if not form.is_valid():
            return render(request, 'users/register.html', context={'form': form})
        form.cleaned_data.__delitem__('confirm_password')
        User.objects.create_user(**form.cleaned_data)
        return redirect('/')
    
def login_view(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'users/login.html', context={'form': form})
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request, 'users/login.html', context={'form': form})
        user = authenticate(**form.cleaned_data)
        if user:
            login(request, user)
        return redirect('/')
    
def logut(request):
    logout(request)
    return redirect('/')