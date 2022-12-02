from django.shortcuts import render, redirect
#from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def index(request):
    return render(request, 'network/index.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request, f'User {username} created')
            return redirect('network:index')
    else:
        form = UserCreationForm()
    return render(request, 'network/register.html', {'form': form})


def profile(request):
    return render(request, 'network/profile.html')