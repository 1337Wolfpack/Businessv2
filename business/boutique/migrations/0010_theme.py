# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0009_auto_20171120_2054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('bgprimary', models.CharField(max_length=200)),
                ('bgsecondary', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=200)),
            ],
        ),
    ]