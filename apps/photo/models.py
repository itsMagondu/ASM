from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailadmin.edit_handlers import (FieldPanel,
                                                PageChooserPanel)

from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page

from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from wagtail.wagtailsearch import index

from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey

from taggit.models import Tag, TaggedItemBase

class PhotoTag(TaggedItemBase):
    content_object = ParentalKey('photo.Photo', related_name='tagged_items')

class Category(Page):
    name = models.CharField(max_length=200)
    description = RichTextField(blank=True)

    search_fields = Page.search_fields + (
        index.SearchField('name'),
        index.SearchField('description'),
    )

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('description', classname="full"),
    ]

class Photo(Page):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
        )
    date = models.DateField("Post date")
    date_taken = models.DateField("Post Taken")
    description = RichTextField(blank=True)
    tags = ClusterTaggableManager(through=PhotoTag, blank=True)

    #This should only be seen by the Admin
    approved = models.BooleanField(default=False)
    approval_date = models.DateField("Approval date")
    
    category = models.ForeignKey('photo.Category', null=True, blank=True ,related_name='+',on_delete=models.SET_NULL )
    
    dpi = models.IntegerField(default=0)
    people_in_pic = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    
    #This should be added automatically from the image
    format = models.CharField(max_length=20)
    
    search_fields = Page.search_fields + (
        index.SearchField('description'),
        index.SearchField('format'),
    )

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        ImageChooserPanel('image'),
        FieldPanel('date_taken'),
        PageChooserPanel('category'),
        FieldPanel('description'),
        FieldPanel('format'),
        FieldPanel('dpi'),
        FieldPanel('people_in_pic'),
        FieldPanel('price'),
    ]


Photo.promote_panels = Page.promote_panels +[
    FieldPanel('tags'),
]
