# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='name',
        ),
        migrations.AddField(
            model_name='photo',
            name='dpi',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='photo',
            name='people_attribute',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='photo',
            name='people_in_picture',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='photo',
            name='slug',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='photo',
            name='title',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(blank=True, to='photo.Category', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='photo',
            name='category',
            field=models.ForeignKey(blank=True, to='photo.Category', null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='description',
            field=models.TextField(),
        ),
    ]
