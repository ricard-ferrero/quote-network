from django.shortcuts import render, redirect
#from django.http import HttpResponse

from .forms import UserRegisterForm
from django.contrib import messages

from .models import Profile
from django.contrib.auth.models import User

def index(request):
    return render(request, 'network/index.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            user = User.objects.get(username=username)
            profile = Profile.objects.get(user_id=user.id)
            profile.quote = form.cleaned_data['quote']
            profile.author_quote = form.cleaned_data['author']
            profile.save()
            messages.success(request, f'User {username} created')
            return redirect('network:index')
    else:
        form = UserRegisterForm()
    return render(request, 'network/register.html', {'form': form})


def profile(request):
    return render(request, 'network/profile.html')