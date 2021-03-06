# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-12 16:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('quantity', models.IntegerField()),
                ('model_id', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'purchase',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(max_length=250)),
                ('supplier_mail', models.EmailField(max_length=254)),
                ('supplier_stock', models.IntegerField()),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Purchase.Purchase')),
            ],
            options={
                'db_table': 'supplier',
            },
        ),
    ]
