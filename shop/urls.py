from django.contrib import admin
from django.urls import path
from . import views
from shop.controller import authview,cart

urlpatterns = [
    path('admin/',admin.site.urls),
    path("",views.shop, name="shop"),
    
    path("register/",authview.register, name="register"),
    path("logout/",authview.logoutpage, name="logout"),
    path("add/",views.add_product, name="add"),
    path("shop/",views.shop, name="shop"),
    path("shop/<str:name>",views.shopview, name="shopview"),
    path("cart/",cart.viewcart, name="cart"),
    path("add-to-cart",cart.addtocart, name="addtocart"),
    path('shop/update/<int:pk>',views.product_update,name='product_update'),
    path('shop/delete/<int:pk>',views.shop_delete,name='shop-delete'),

    
]