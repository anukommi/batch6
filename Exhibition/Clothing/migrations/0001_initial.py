# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-10 12:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ladies_wear',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('cloth_collection', models.IntegerField(default=34)),
            ],
            options={
                'db_table': 'Ladies_wear',
            },
        ),
        migrations.CreateModel(
            name='Mens_wear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('cloth_collection', models.IntegerField(default=34)),
            ],
            options={
                'db_table': 'Mens_wear',
            },
        ),
    ]
