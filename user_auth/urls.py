from django.urls import path
from django.conf.urls import include
from user_auth import views

app_name = 'user_auth'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('special/', views.special, name='special'),
    ]