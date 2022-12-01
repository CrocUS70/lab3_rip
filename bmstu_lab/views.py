from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from bmstu_lab.models import views_product, group_products as group_products2, products as products2
from datetime import date
from rest_framework import viewsets
from bmstu_lab.serializers import ViewsSerializer, GroupSerializer, ProductsSerializer

class ViewsViewSet(viewsets.ModelViewSet):
    queryset = views_product.objects.all()
    serializer_class = ViewsSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = group_products2.objects.all()
    serializer_class = GroupSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = products2.objects.all()
    serializer_class = ProductsSerializer

def home(request):
    return redirect('views_products')

def views_products(request):
    return render(request, 'views_products.html', {'data': {
        'current_date': date.today().strftime('%d.%m.%y'),
        'view': views_product.objects.all()
    }})

def group_products(request, id):
    return render(request, 'group_products.html', {'data': {
        'current_date': date.today().strftime('%d.%m.%y'),
        'group': group_products2.objects.filter(views_id=id),
        'v': views_product.objects.get(id=id)
    }})


def products(request, id):
    return render(request, 'products.html', {'data': {
        'current_date': date.today().strftime('%d.%m.%y'),
        'pro': products2.objects.filter(group_id=id),
        'g': group_products2.objects.get(id=id)
    }})


def product(request, id):
    return render(request, 'product.html', {'data': {
        'current_date': date.today().strftime('%d.%m.%y'),
        'prod': products2.objects.filter(id=id)[0],
        'p': products2.objects.get(id=id)
    }})