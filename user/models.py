from django.db import models
class Product(models.Model):
    product_name=models.CharField(max_length=100)
    price=models.FloatField()
    description=models.TextField()
    image=models.ImageField(upload_to="Product_Images")
    offer=models.BooleanField(default=True)

class Register(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)

class diabetes(models.Model):
    preg=models.FloatField()
    glucose=models.FloatField()
    bp=models.FloatField()
    skin=models.FloatField()
    pedigree=models.FloatField()
    age=models.FloatField()


# Create your models here.
