from django.db import models
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    nom = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    icon = models.CharField(max_length=500)
    def __str__(self):
        return self.nom

class Theme(models.Model):
    name = models.CharField(max_length=200)
    bgprimary = models.CharField(max_length=200)
    bgdark = models.CharField(max_length=200)
    bgsecondary = models.CharField(max_length=200)
    btnprimary = models.CharField(max_length=200)
    btnprimarytextcolor = models.CharField(max_length=200)
    btnsecondary = models.CharField(max_length=200)
    btnsecondarytextcolor = models.CharField(max_length=200)
    btnprimaryhover = models.CharField(max_length=200)
    btnsecondaryhover = models.CharField(max_length=200)
    text1 = models.CharField(max_length=600, null=True)
    text2 = models.CharField(max_length=600,null=True)
    brand = models.CharField(max_length=200,null=True)
    facebook = models.CharField(max_length=200,null=True)
    instagram = models.CharField(max_length=200,null=True)
    twitter = models.CharField(max_length=200,null = True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField(blank = True)
    prix = models.CharField(max_length=200)
    amazonlink = models.CharField(max_length=200)
    category = models.ForeignKey(Category)
    stockVolume = models.CharField(max_length=200)
    shippingVolume = models.CharField(max_length=200)
    shippingCost = models.CharField(max_length=200)
    
    def getPrimaryImage(self):
        images = ProductImage.objects.filter(product=self)[:1]
        return images[0]
        
    def __str__(self):
        return self.nom
    
class SiteImage(models.Model):
    nom = models.CharField(max_length=200)
    image = models.ImageField(upload_to="site")
    
    def __str__(self):
        return self.nom
        
class ImageElement(models.Model):    
    nom = models.CharField(max_length=200)
    divId = models.CharField(max_length=200)
    image = models.ForeignKey(SiteImage)
    
    def __str__(self):
        return "%s dans la div : %s" % (self.image.image.file, self.divId)
        
class ProductImage(models.Model):
    nom = models.CharField(max_length=200)
    image = models.ImageField(upload_to="products")
    product = models.ForeignKey(Product, null=True)
    primary = models.BooleanField(default=True)
    def __str__(self):
        return self.nom

class Box(models.Model):
    nom = models.CharField(max_length=200)
    products = models.ManyToManyField(Product)
    prix = models.CharField(max_length=200)
    shippingCost = models.CharField(max_length=200)
    shippingVolume = models.CharField(max_length=200)
    def __str__(self):
        return self.nom

class Warehouse(models.Model):
    nom = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.nom

class StockItem(models.Model):
    item = models.ForeignKey(Product)
    warehouse = models.ForeignKey(Warehouse, null=True)
    def __str__(self):
        return self.nom


  
class Client(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)



class Order(models.Model):
    client = models.ForeignKey(Client)
    date = models.DateTimeField()

    
class Address(models.Model):
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    street_line_1 = models.CharField(max_length=200)
    postalcode = models.CharField(max_length=200)
    def __str__(self):
        return '%s, %s, %s, %s' % (self.street_line_1, self.postalcode, self.city, self.country)

