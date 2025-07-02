from django.urls import path
from stockmanager import views

urlpatterns = [
    path('', views.get_stock),
]