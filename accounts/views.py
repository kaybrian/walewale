from django.shortcuts import render, redirect
from .forms import UserRegistrationForm,CustomAuthForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def register(request):
    template_name = 'accounts/register.html'
    form = UserRegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            new_user = form.save()
            messages.success(request, 'Account succesfully created. You can now login')
            return redirect('accounts:login')
    return render(request, template_name,{"form":form})


def login_user(request):
    form = CustomAuthForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(email=cd['email'], password=cd['password'])
            print(f'User detials -> {cd["email"]} and password -> {cd["password"]}')
            if user is not None:
                login(request, user)
                return redirect('accounts:dashboard')
            else:
                messages.error(request, 'Account does not exist')
    return render(request, "accounts/login.html", context = {"form":form})


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')


