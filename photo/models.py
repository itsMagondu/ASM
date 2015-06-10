from siteAdmin.models import UserProfile
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    active = models.BooleanField(default = None)
    
    def __unicode__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category,null=True,blank=True)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    active = models.BooleanField(default = None)
    
    def __unicode__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add = True)
    active = models.BooleanField(default = None)

    def __unicode__(self):
        return self.name    

# Create your models here.
class Photo(models.Model):
    title = models.CharField(max_length=100,null=True,blank=True)
    slug = models.CharField(max_length=100,null=True,blank=True)
    regularImage  = models.ImageField(upload_to='photos/regular/%Y/%m/%d')
    supersizeImage  = models.ImageField(upload_to='photos/supersize/%Y/%m/%d',null=True,blank=True)
    previewImage  = models.ImageField(upload_to='photos/preview/%Y/%m/%d',null=True,blank=True)
    description = models.CharField(max_length=100,null=True,blank=True)
    uploaded_by =  models.ForeignKey('siteAdmin.UserProfile',related_name = 'uploaded')
    price = models.IntegerField(default=0)
    dpi = models.IntegerField(default=0)
    category = models.ForeignKey(Category,null=True,blank=True)
    subcategory = models.ForeignKey(SubCategory,null=True,blank=True)
    format = models.CharField(max_length=10,null=True)
    date = models.DateTimeField(auto_now_add = True)
    date_taken = models.DateTimeField(auto_now_add = True)
    people_in_picture = models.IntegerField(default = 0)
    people_attribute = models.CharField(max_length=100,null=True,blank=True)
    active = models.BooleanField(default = None)
    approved = models.BooleanField(default = None) 
    approved_by = models.ForeignKey('siteAdmin.UserProfile',related_name = 'approved',null=True,blank=True)
    approved_on = models.DateTimeField(null=True)
    
class Purchases(models.Model):
    photo = models.ForeignKey(Photo)
    buyer = models.ForeignKey('siteAdmin.UserProfile',related_name="profile")
    date = models.DateTimeField(auto_now_add = True)
    active = models.BooleanField(default = None)
    
class TagAssignment():
    tag = models.ForeignKey(Tag)
    photo = models.ForeignKey(Photo)
    date = models.DateTimeField(auto_now_add = True)
    active = models.BooleanField(default = None)
