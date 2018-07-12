# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Product(models.Model):
	name=models.CharField(max_length=250)
	cost=models.IntegerField()
	
	class Meta:
		db_table="product"

class Specification(models.Model):
	model=models.CharField(max_length=290)
	product=models.ManyToManyField(Product)
	product=models.ForeignKey(Product)

	class Meta:
		db_table="specification"



