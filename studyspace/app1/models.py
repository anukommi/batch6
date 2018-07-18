# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class StudyHall(models.Model):
	name=models.CharField(max_length=250)
	area=models.TextField()

	def __str__(self):
		return "%s | %s"%(self.name,self.area)

class Expense(models.Model):
	studyhall=models.ForeignKey(StudyHall)
	date=models.DateTimeField()
	name=models.CharField(max_length=250)
	desc=models.TextField(max_length=300)
	value=models.IntegerField()

	def __str__(self):
		return "%s,%s,%s,%s,%s"%(self.studyhall,
			self.date,
			self.name,
			self.desc,
			self.value)

class Course(models.Model):
	course=models.CharField(max_length=250)

	def __str__(self):
		return "%s"%(self.course)

class Student(models.Model):
	name=models.CharField(max_length=250)
	phone=models.CharField(max_length=250)
	email=models.CharField(max_length=250)
	address=models.TextField()

	def __str__(self):
		return "%s,%s,%s,%s"%(self.name,
			self.phone,
			self.email,
			self.address)

class Enquiry(models.Model):
	name=models.CharField(max_length=250)
	course=models.ForeignKey(Course)
	student=models.ForeignKey(Student)

	def __str__(self):
		return "%s,%s,%s"%(self.name,
			self.course,
			self.student)
