from django.db import models
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    nom = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    icon = models.CharField(max_length=500)
    def __str__(self):
        return self.nom
    

class Product(models.Model):
    nom = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    prix = models.CharField(max_length=200)
    amazonlink =models.CharField(max_length=200)
    category = models.ForeignKey(Category)
    def __str__(self):
        return self.nom
    

