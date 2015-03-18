# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_auto_20150210_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='approved_by',
            field=models.ForeignKey(related_name='approved', blank=True, to='siteAdmin.UserProfile', null=True),
            preserve_default=True,
        ),
    ]
