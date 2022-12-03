from django.shortcuts import render, redirect
#from django.http import HttpResponse

from .forms import UserRegisterForm
from django.contrib import messages


def index(request):
    return render(request, 'network/index.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'User {username} created')
            return redirect('network:index')
    else:
        form = UserRegisterForm()
    return render(request, 'network/register.html', {'form': form})


def profile(request):
    return render(request, 'network/profile.html')