# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-12 09:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_image_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image_url',
        ),
        migrations.AddField(
            model_name='image',
            name='image_link',
            field=models.CharField(default='link not available', max_length=500),
            preserve_default=False,
        ),
    ]
