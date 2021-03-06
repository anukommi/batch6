# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-11 09:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commodities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('quantity', models.CharField(max_length=200)),
                ('cost', models.IntegerField()),
            ],
            options={
                'db_table': 'commodities',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('name', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('mobile_number', models.IntegerField()),
                ('mail_id', models.CharField(max_length=250)),
                ('address', models.TextField()),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='Salesorder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('type', models.CharField(choices=[('online', 'Online Payment'), ('COD', 'Cash On Delivery')], max_length=6)),
                ('commodities', models.ManyToManyField(to='Groceries.Commodities')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Groceries.Customer')),
            ],
            options={
                'db_table': 'salesorder',
            },
        ),
    ]
