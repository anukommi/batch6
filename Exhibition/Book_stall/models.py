# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Kids_Sale(models.Model):
	name=models.CharField(max_length=250)
	start_time=models.DateTimeField("Opening Time")
	End_time=models.DateTimeField("Closing Time")
	Languages=models.IntegerField(default=10)
	class Meta:
		db_table="Kids_Sale"


#Adult_Sale has own primary key
class Adult_Sale(models.Model):
	name=models.CharField(max_length=250, primary_key=True)
	start_time=models.DateTimeField("Opening Time")
	End_time=models.DateTimeField("Closing Time")
	Languages=models.IntegerField(default=10)

	class Meta:
		db_table="Adult_Sale"

	

