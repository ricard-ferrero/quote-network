from django.shortcuts import render, redirect
#from django.http import HttpResponse

from .forms import UserRegisterForm
from django.contrib import messages

from .models import *
from django.contrib.auth.models import User

def index(request):
    users_list = User.objects.all()
    return render(request, 'network/index.html', {'users_list': users_list})


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


def profile(request, user_name=None):
    current_user = request.user
    if user_name and user_name != current_user.username:
        profile = User.objects.get(username=user_name)
    else:
        profile = current_user
    return render(request, 'network/profile.html', {'profile': profile})


def follow(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user
    rel = Relationship(from_user=current_user, to_user=to_user_id)
    rel.save()
    messages.success(request, f'Following {username}')
    return redirect('network:index')


def unfollow(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user.id
    rel = Relationship.objects.filter(from_user=current_user.id, to_user=to_user_id).get()
    rel.delete()
    messages.success(request, f'Unfollow {username}')
    return redirect('network:index')