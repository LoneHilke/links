from django.urls import path
from . import views

urlpatterns = [
  path('', views.python_list, name='python_list'),
  path('python/<int:pk>/', views.python_detail, name='python_detail'),
  path('python/new/', views.python_new, name='python_new'),
  path('python/<int:pk>/edit/', views.python_edit, name='python_edit'),
]