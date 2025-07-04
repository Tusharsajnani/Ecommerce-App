
from django.db import models
# Create your models here. #name,description ,price,stock&category
class Product(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=500)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField()
    category= models.CharField(max_length=100)


    def __str__(self):
        return self.name