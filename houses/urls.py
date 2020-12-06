from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_houses, name='list houses'),
    path('create/', views.create_house, name='post house'),
]
