# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteAdmin', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=None)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('regularImage', models.ImageField(upload_to=b'photos/regular/%Y/%m/%d')),
                ('supersizeImage', models.ImageField(null=True, upload_to=b'photos/supersize/%Y/%m/%d', blank=True)),
                ('previewImage', models.ImageField(null=True, upload_to=b'photos/preview/%Y/%m/%d', blank=True)),
                ('description', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('format', models.CharField(max_length=10, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('date_taken', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=None)),
                ('approved', models.BooleanField(default=None)),
                ('approved_on', models.DateTimeField(null=True)),
                ('approved_by', models.ForeignKey(related_name=b'approved', to='siteAdmin.UserProfile')),
                ('category', models.ForeignKey(to='photo.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Purchases',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=None)),
                ('buyer', models.ForeignKey(to='siteAdmin.UserProfile')),
                ('photo', models.ForeignKey(to='photo.Photo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=None)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=None)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='photo',
            name='subcategory',
            field=models.ForeignKey(blank=True, to='photo.SubCategory', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='photo',
            name='uploaded_by',
            field=models.ForeignKey(related_name=b'uploaded', to='siteAdmin.UserProfile'),
            preserve_default=True,
        ),
    ]
