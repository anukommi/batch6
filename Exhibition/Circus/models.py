# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Morning_shows(models.Model):
	name=models.CharField(max_length=120)
	shows=models.IntegerField(default=12)
	ticket_price=models.IntegerField(default=100)

	class Meta:
		db_table = "Morning_shows"

class Night_shows(models.Model):
	name=models.CharField(max_length=120, primary_key=True)
	shows=models.IntegerField(default=8)
	ticket_price=models.IntegerField(default=150)

	class Meta:
		db_table = "Night_shows"