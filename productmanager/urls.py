
from django.urls import path
from productmanager import views

urlpatterns = [
    path('<id>', views.show_product_by_id),
    path('', views.show_all_products)
]