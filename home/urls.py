from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('register/', views.RegisterView, name='register'),
    path('list/', views.ListView, name='list'),
]