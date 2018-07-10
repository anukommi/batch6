# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class South_Indian(models.Model):
	name=models.CharField(max_length=300)
	food_items=models.IntegerField(default=400)
	discount=models.IntegerField(default=100)

	class meta:
		db_table="South_Indian"


class North_Indian(models.Model):
	name=models.CharField(max_length=300, primary_key=True)
	food_items=models.IntegerField(default=400)
	discount=models.IntegerField(default=100)

	class meta:
		db_table="North_Indian"
