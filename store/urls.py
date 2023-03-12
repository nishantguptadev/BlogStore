from django.urls import path
from store import views

urlpatterns = [
    path("", views.index, name='index'),
    path("cart/", views.cart, name='cart'),
    path("checkout/", views.checkout, name='checkout'),
    path("search/", views.search, name='search'),
    path("products/<int:myid>", views.productView ,name="ProductView"),
]