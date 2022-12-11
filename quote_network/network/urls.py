from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'network'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='network/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='network/logout.html'), name='logout'),
    path('follow/<str:username>/', views.follow, name='follow'),
    path('unfollow/<str:username>/', views.unfollow, name='unfollow'),
    
    # 'profile' must be allways THE LAST
    path('<str:profile>/', views.profile, name='profile'),
]