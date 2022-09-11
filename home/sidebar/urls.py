from django.urls import path
from . import views

urlpatterns = [
  path('', views.sidebar_list, name='sidebar_list'),
  path('sidebar/<int:pk>/', views.sidebar_detail, name='sidebar_detail'),
  path('sidebar/new/', views.sidebar_new, name='sidebar_new'),
  path('sidebar/<int:pk>/edit/', views.sidebar_edit, name='sidebar_edit'),
]