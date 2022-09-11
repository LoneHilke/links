from django.urls import path
from . import views

urlpatterns = [
  path('', views.jango_list, name='jango_list'),
  path('jango/<int:pk>/', views.jango_detail, name='jango_detail'),
  path('jango/new/', views.jango_new, name='jango_new'),
  path('jango/<int:pk>/edit/', views.jango_edit, name='jango_edit'),
]