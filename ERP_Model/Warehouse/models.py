# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Location(models.Model):
	warehouse_name=models.CharField(max_length=250)
	warehouse_address=models.TextField()
	mobile=models.CharField(max_length=250)
	email=models.EmailField()

	class Meta:
		db_table="location"


class Warehouse(models.Model):
	manager_name=models.CharField(max_length=250)
	warehou_key=models.ForeignKey(Location)
	workers_count=models.IntegerField()	
	workers_salary=models.IntegerField()
	rack_storage=models.IntegerField()	
	# warehou=models.ManyToManyField(Location)

	class Meta:
		db_table="warehouse"

