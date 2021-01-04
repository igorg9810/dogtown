from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('akita', views.akita, name='akita'),
    path('store', views.store, name='store'),
]