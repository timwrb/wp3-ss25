from django.urls import include

from . import views

from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('convert-cart', views.convert_cart),
    path('add-to-cart', views.add_to_cart),
    path('', views.show_cart),
    path('<id>', views.show_cart_detail)
]
