from django.db import models
from django.contrib.auth.models import User
import datetime

class UserProfile(models.Model):
    '''Extended user details. Figure out how to do this.'''
    user = models.OneToOneField(User)
        
    occupation = models.TextField(null = True)
    bio = models.TextField(null=True,blank=True)
    isBuyer = models.BooleanField(default = False)
    isSeller = models.BooleanField(default = False)
    credit = models.IntegerField(default = 0)
    balance = models.IntegerField(default = 0)
    country = models.TextField(null = True)
    
    def __unicode__(self):
        return self.user.username
