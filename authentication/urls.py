from django.urls import path
from . import views

urlpatterns = [
    path('auth/', views.auth, name='auth'),
]