from django.contrib import admin
from photo.models import *

def mark_active(modeladmin, request, queryset):
        queryset.update(active = True)

def mark_inactive(modeladmin, request, queryset):
        queryset.update(active = False)


# Register your models here.
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'dpi', 'date', 'active','price')
    search_fields = ['title', 'price']
    actions = [mark_inactive,mark_active]   

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date', 'active')
    search_fields = ['name', 'description']
    actions = [mark_inactive,mark_active]       

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date', 'active')
    search_fields = ['name', 'description']
    actions = [mark_inactive,mark_active]       

class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date', 'active')
    search_fields = ['name', 'description']
    actions = [mark_inactive,mark_active]       

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Tag, TagAdmin)
