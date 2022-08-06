from django.shortcuts import render, redirect
from .forms import UserRegistrationForm



def register(request):
    template_name = 'accounts/register.html'
    form = UserRegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            new_user = form.save()
            return redirect('accounts:register')
    return render(request, template_name,{"form":form})


