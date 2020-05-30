from django.urls import path

from . import views

urlpatterns = [
    # ex: /main/
    path('main/', views.index, name='index'),
    path('details/', views.details, name='details'),
    path('search/', views.search, name='search'),
    # ex: /main/newItem/
    path('generate/', views.generate, name='generate'),
    path('newItem/', views.newItemPage, name='newItem'),
    # ex: /main/43/
    path('<int:adID>/', views.details, name='details'),
]
