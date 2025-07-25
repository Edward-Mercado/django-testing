from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('', views.main, name='main'),
    path('testing/', views.testing, name='testing'),
]