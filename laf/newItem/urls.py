from django.urls import path
from . import views

urlpatterns = [
    path('', views.newItem, name='newItem'),
]
