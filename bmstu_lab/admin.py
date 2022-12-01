from django.contrib import admin
from .models import views_product, group_products, products
# Register your models here.
admin.site.register(views_product)
admin.site.register(group_products)
admin.site.register(products)