# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 19:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0005_auto_20171115_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
