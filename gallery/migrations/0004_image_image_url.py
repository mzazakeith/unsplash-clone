# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-12 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20180711_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image_url',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]