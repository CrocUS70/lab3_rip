from bmstu_lab.models import views_product, group_products, products
from rest_framework import serializers


class ViewsSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = views_product
        # Поля, которые мы сериализуем
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = group_products
        # Поля, которые мы сериализуем
        fields = '__all__'

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = products
        # Поля, которые мы сериализуем
        fields = '__all__'