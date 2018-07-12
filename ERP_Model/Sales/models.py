# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Customer(models.Model):
	name=models.CharField(max_length=250)
	mobile_num=models.IntegerField()
	email_id=models.EmailField()	
	billing_address=models.TextField()
	shipping_address=models.TextField()

	class Meta:
		db_table="customer"

class Sales_order(models.Model):
	quantity=models.IntegerField()
	payment_method=[('online','Online Payment'),('COD','Cash On Delivery')]
	customer=models.ForeignKey(Customer)
	customer=models.ManyToManyField(Customer)	
	sales_person=models.CharField(max_length=250)
	shipping_method=models.CharField(max_length=250)
	delivery_date=models.CharField(max_length=250)
	types=models.CharField(choices=payment_method, max_length=10)
	
	class Meta:
		db_table="sales_order"

