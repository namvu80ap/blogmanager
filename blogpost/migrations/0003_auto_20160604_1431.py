# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-04 14:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0002_auto_20160604_1430'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='image',
            new_name='imageUrl',
        ),
    ]
