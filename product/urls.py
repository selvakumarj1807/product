"""
URL configuration for product project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from productapp import views as shop_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', shop_views.login_view, name='login'),
    path('logout/', shop_views.logout_view, name='logout'),
    path('products/', shop_views.product_list, name='products'),
    path('add_to_cart/', shop_views.add_to_cart, name='add_to_cart'),
    path('cart/', shop_views.cart_view, name='cart'),
]

