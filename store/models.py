from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Product(models.Model):
    name= models.CharField(max_length=200, null=True)
    category=models.CharField(max_length=50,default="")
    price= models.FloatField()
    desc=models.CharField(max_length=300, default="")
    digital = models.BooleanField(default=False, null=True, blank=False)
    image=models.ImageField(upload_to="images", null=True, blank= True, default='')

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=""
        return url



class Order(models.Model): 
    order_id = models.AutoField(primary_key=True)
    items_json= models.CharField(max_length=5000)
    amount=models.IntegerField(default=0)
    name= models.CharField(max_length=100)
    email= models.CharField(max_length=111)
    address= models.CharField(max_length=111)
    city= models.CharField(max_length=111)
    state= models.CharField(max_length=122)
    zip_code= models.CharField(max_length=111,default="")
    phone= models.CharField(max_length=111,default="")

    def __str__(self):
        return self.name



    