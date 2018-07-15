# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Purchase(models.Model):
	name=models.CharField(max_length=250)
	quantity=models.IntegerField()
	model_id=models.CharField(max_length=250)

	class Meta:
		db_table="purchase"

class Supplier(models.Model):
	supplier_name=models.CharField(max_length=250)
	supplier_mail=models.EmailField()
	supplier_stock=models.IntegerField()
	product_name=models.ForeignKey(Purchase)
	product_name=models.ManyToManyField(Purchase)
	

	class Meta:
		db_table="supplier"


