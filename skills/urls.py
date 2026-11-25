from django.urls import path
from . import views

urlpatterns = [
    path('', views.skill_list, name='skill_list'),
    path('ajouter/', views.skill_create, name='skill_create'),
    path('modifier/<int:pk>/', views.skill_update, name='skill_update'),
    path('supprimer/<int:pk>/', views.skill_delete, name='skill_delete'),
]