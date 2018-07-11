# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Item(models.Model):
	name=models.CharField(max_length=250)
	quantity=models.CharField(max_length=200)
	cost=models.IntegerField()

	class Meta:
		db_table = "item"

class Customer(models.Model):
	name=models.CharField(max_length=250, primary_key=True)
	mail_id=models.CharField(max_length=250)
	mobile_number=models.IntegerField()
	address=models.TextField()

	class Meta:
		db_table = "customer"


class Salesorder(models.Model):
	salesorder_types=[("online", "Online payment"),("COD", "Cash On Delivery")]
	name=models.CharField(max_length=250)
	product=models.ManyToManyField(Item)
	customer=models.ForeignKey(Customer)
	type=models.CharField(choices=salesorder_types,max_length=6)

	class Meta:
		db_table="salesorder"

	
