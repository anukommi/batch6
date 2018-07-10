# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Adventure_games(models.Model):
	name=models.CharField(max_length=200)
	games_count=models.IntegerField(default=33)
	child_entry_ticket=models.IntegerField(default=800)
	adult_entry_ticket=models.IntegerField(default=1500)

	class Meta:
		db_table="Adventure_games"

class Water_games(models.Model):
	name=models.CharField(max_length=200, primary_key=True)
	games_count=models.IntegerField(default=20)
	child_entry_ticket=models.IntegerField(default=700)
	adult_entry_ticket=models.IntegerField(default=1200)

	class Meta:
		db_table="Water_games"
