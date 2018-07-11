# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# from Vegetables.models import Customer

# Create your models here.
class Commodities(models.Model):
	name=models.CharField(max_length=250)
	quantity=models.CharField(max_length=200)
	cost=models.IntegerField()

	class Meta:
		db_table="commodities"


class Customer_Groceries(models.Model):
	name=models.CharField(max_length=250, primary_key=True)
	mobile_number=models.IntegerField()
	mail_id=models.CharField(max_length=250)
	address=models.TextField()

	class Meta:
		db_table="customer_groceries"

class Salesorder(models.Model):
	salesorder_types = [("online", "Online Payment"), ("COD", "Cash On Delivery")]
	name = models.CharField(max_length=250)
	commodities=models.ManyToManyField(Commodities)
	customer_groceries=models.ForeignKey(Customer_Groceries)
	type=models.CharField(choices=salesorder_types, max_length=6)

	class Meta:
		db_table="salesorder"
