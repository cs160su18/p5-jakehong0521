from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('need/', views.need, name='need'),
  path('history/', views.history, name='history'),
  path('items/', views.items, name='items'),
  path('users/', views.users, name='users')
]