# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Mens_wear(models.Model):
	name=models.CharField(max_length=200)
	cloth_collection=models.IntegerField(default=34)
	#last_date=models.DateField()
	#last_date=models.DateField(input_formats=settings.DATE_INPUT_FORMATS)
	#last_date = models.DateField(blank=True, null=True,verbose_name=last_date)

	class Meta:
		db_table = "Mens_wear"


class Ladies_wear(models.Model):
	name=models.CharField(max_length=200, primary_key=True)
	cloth_collection=models.IntegerField(default=34)
	#last_date=models.DateField()
	#last_date=model.DateField(input_formats=settings.DATE_INPUT_FORMATS)
	#last_date = models.DateField(blank=True, null=True,verbose_name=last_date)

	class Meta:
		db_table = "Ladies_wear"

