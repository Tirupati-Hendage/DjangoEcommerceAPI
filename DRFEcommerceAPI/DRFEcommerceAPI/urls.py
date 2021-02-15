"""DRFEcommerceAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from DjangoAPIApp import views

router1 = routers.DefaultRouter()
router2 = routers.DefaultRouter()
router3 = routers.DefaultRouter()

router1.register('category', views.CategoryModelViewSet, basename='category')
router2.register('books', views.BookModelViewSet, basename='book')
router3.register('products', views.ProductModelViewSet, basename='product')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router1.urls)),
    path('book/',include(router2.urls)),
    path('product/',include(router3.urls)),
    path('auth/', include('rest_framework.urls'), name='rest_frameworks')
]
