from django.db import models

# Create your models here.

class GetDb(models.Model):
    Name = models.CharField(max_length=50, null=True, blank=True)
    Email = models.CharField(max_length=50, null=True, blank=True)
    Description = models.CharField(max_length=200, null=True, blank=True)

class SignupDb(models.Model):
    Name = models.CharField(max_length=50, null=True, blank=True)
    Mobile = models.IntegerField( null=True, blank=True)
    Email = models.CharField(max_length=50, null=True, blank=True)
    Pswd = models.CharField(max_length=50, null=True, blank=True)
    CfrmPswd = models.CharField(max_length=50, null=True, blank=True)

class ServiceDb(models.Model):
    Name = models.CharField(max_length=50, null=True, blank=True)    
    Email = models.CharField(max_length=50, null=True, blank=True)    
    Select = models.CharField(max_length=50, null=True, blank=True)    
    Phone = models.CharField(max_length=50, null=True, blank=True)    
    Address = models.CharField(max_length=500, null=True, blank=True)    
    