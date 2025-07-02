from django.urls import include

from . import views

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('<id>', views.show_address_by_id),
    path('', views.show_all_addresses)
]
