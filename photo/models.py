from siteAdmin.models import UserProfile
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add = True)
    active = models.BooleanField(default = None)

class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add = True)
    active = models.BooleanField(default = None)
    
# Create your models here.
class Photo(models.Model):
    name = models.CharField(max_length=50)
    file  = models.FileField(upload_to='photos/main/%Y/%m/%d')
    previewfile  = models.FileField(upload_to='photos/preview/%Y/%m/%d')
    description = models.CharField(max_length=100)
    uploaded_by =  models.ForeignKey('siteAdmin.UserProfile',related_name = 'uploaded')
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category)
    subcategory = models.ForeignKey(SubCategory,null=True,blank=True)
    #tags = models.TextField(null=True,blank=True)
    format = models.CharField(max_length=10,null=True)
    date = models.DateTimeField(auto_now_add = True)
    active = models.BooleanField(default = None)
    approved = models.BooleanField(default = None) 
    approved_by = models.ForeignKey('siteAdmin.UserProfile',related_name = 'approved')
    approved_on = models.DateTimeField(null=True)
    
class Purchases(models.Model):
    photo = models.ForeignKey(Photo)
    buyer = models.ForeignKey('siteAdmin.UserProfile')
    date = models.DateTimeField(auto_now_add = True)
    active = models.BooleanField(default = None)
    
class Tag(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add = True)
    active = models.BooleanField(default = None)
    
class TagAssignment():
    tag = models.ForeignKey(Tag)
    photo = models.ForeignKey(Photo)
    date = models.DateTimeField(auto_now_add = True)
    active = models.BooleanField(default = None)
