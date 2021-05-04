from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),

    # Product id must be an integer or the 'add' url
    # would be parsed as a product id and throw an error
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
]