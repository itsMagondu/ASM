from siteAdmin.models import UserProfile
from django.db import models

# Create your models here.
class Photo(models.Model):
    name = models.CharField(max_length=50)
    file  = models.FileField(upload_to='photos/%Y/%m/%d')
    description = models.CharField(max_length=100)
    uploaded_by =  models.ForeignKey('siteAdmin.UserProfile')
    price = models.IntegerField(default=0)
    category = models.CharField(max_length=50)
    tags = models.TextField(null=True,blank=True)
    format = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add = True)
    active = models.BooleanField(default = None)
    
class Purchases(models.Model):
    photo = models.ForeignKey(Photo)
    buyer = models.ForeignKey('siteAdmin.UserProfile')
    date = models.DateTimeField(auto_now_add = True)
    
