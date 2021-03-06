# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-10 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adventure_games',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('games_count', models.IntegerField(default=33)),
                ('child_entry_ticket', models.IntegerField(default=800)),
                ('adult_entry_ticket', models.IntegerField(default=1500)),
            ],
            options={
                'db_table': 'Adventure_games',
            },
        ),
        migrations.CreateModel(
            name='Water_games',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('games_count', models.IntegerField(default=20)),
                ('child_entry_ticket', models.IntegerField(default=700)),
                ('adult_entry_ticket', models.IntegerField(default=1200)),
            ],
            options={
                'db_table': 'Water_games',
            },
        ),
    ]
