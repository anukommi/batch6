# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-11 07:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vegetables', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.CharField(max_length=200),
        ),
    ]
