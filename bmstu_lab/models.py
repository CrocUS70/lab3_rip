from django.db import models

# Create your models here.
class views_product(models.Model):
    name_views = models.CharField(max_length=100)



class group_products(models.Model):
    views = models.ForeignKey(views_product, on_delete=models.CASCADE)
    name_group = models.CharField(max_length=100)


class products(models.Model):
    group = models.ForeignKey(group_products, on_delete=models.CASCADE)
    name_product = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
