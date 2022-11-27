from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def hello_world(request):
    return HttpResponse('<h1>Hello World!</h1>')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            message.success(request, f'User {username} created')
    else:
        form = UserCreationForm()
    return render(request, 'network/register.html', {'form': form})


def profile(request):
    return render(request, 'network/profile.html')