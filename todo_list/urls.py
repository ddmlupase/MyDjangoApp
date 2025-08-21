from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('delete/<int:list_id>/', views.delete, name='delete'),
    path('strike/<int:list_id>/', views.strike, name='strike'),
    path('unstrike/<int:list_id>/', views.unstrike, name='unstrike'),
]
