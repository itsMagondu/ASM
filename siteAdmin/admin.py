from django.contrib import admin
from siteAdmin.models import *

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'credit', 'occupation')

admin.site.register(UserProfile, UserProfileAdmin)
