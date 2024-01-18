from django.db import models

# Create your models here.


class userDb(models.Model):
    Name = models.CharField(max_length=50, null=True, blank=True)
    Category = models.CharField(max_length=50, null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    Email = models.CharField(max_length=50, null=True, blank=True)
    Password = models.CharField(max_length=50, null=True, blank=True)
    Description = models.CharField(max_length=50, null=True, blank=True)
    Image = models.ImageField(upload_to='DCIM', null=True, blank=True)

class CatDb(models.Model):
    Cat_Name = models.CharField(max_length=50, null=True, blank=True)   
    Cat_Desc = models.CharField(max_length=100, null=True, blank=True)
    Cat_Image = models.ImageField(upload_to='category', null=True, blank=True)

class ProductDb(models.Model):   
    ProCat_Name = models.CharField(max_length=50, null=True, blank=True) 
    ProName = models.CharField(max_length=50, null=True, blank=True)
    ProPrice = models.IntegerField(null=True, blank=True)
    Pro_Desc = models.CharField(max_length=100, null=True, blank=True)
    Pro_Image = models.ImageField(upload_to='products', null=True, blank=True)