"""bmstu__2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path
from bmstu_lab import views
from rest_framework import routers
from bmstu_lab.views import *

router = routers.DefaultRouter()
router.register(r'views', ViewsViewSet)
router.register(r'group', GroupViewSet)
router.register(r'products', ProductsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('admin/', admin.site.urls),
    path('', views.home),
    path('views_product/', views.views_products, name='views_products'),
    path('group_products/<int:id>', views.group_products, name='group_products'),
    path('products/<int:id>', views.products, name='products'),
    path('product/<int:id>', views.product, name='product'),
]
