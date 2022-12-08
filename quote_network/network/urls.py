from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'network'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/<str:user_name>/', views.profile, name='profile'),
    path('login/', LoginView.as_view(template_name='network/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='network/logout.html'), name='logout'),
]