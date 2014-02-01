from django.db import models
from django.contrib.auth.models import User
import datetime

class UserProfile(models.Model):
    '''Extended user details.'''
    user = models.ForeignKey(User, unique = True)
        
    occupation = models.TextField(null = True)
    isBuyer = models.BooleanField(default = False)
    isSeller = models.BooleanField(default = False)
    credit = models.IntegerField(default = 0)
    balance = models.IntegerField(default = 0)
    canView = models.BooleanField(default = True)
    country = models.TextField(null = True)
    
    def __unicode__(self):
        return self.user
