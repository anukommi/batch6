# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Account(models.Model):
	account_name=models.CharField(max_length=250)
	manager=models.CharField(max_length=250)
	transport=models.CharField(max_length=250)
	labor_salary=models.IntegerField()
	cur_year_earnings=models.IntegerField()

	class Meta:
		db_table="account"

class Journals(models.Model):
	journal_name=models.CharField(max_length=250)
	journal_desc=models.TextField()
	account=models.ForeignKey(Account)
	account=models.ManyToManyField(Account)

	class Meta:
		db_table="journals"

	

