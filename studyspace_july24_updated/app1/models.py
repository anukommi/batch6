# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NameModel(models.Model):
	#abstract model which dont create table in background
	name=models.CharField(max_length=250, unique=True)

	class Meta:
		abstract=True

class StudyHall(NameModel):
	# Now StudyHall is inherited from StudyHall class
	# name = models.CharField(max_length=50)
	area = models.TextField(max_length=250)
	def __str__(self):
		return "%s|%s"%(self.name, self.area)

class Expenses(NameModel):
	studyhall = models.ForeignKey(StudyHall)
	date = models.DateTimeField()
	# name=models.CharField(max_length=250)
	desc = models.TextField(max_length=250)
	value= models.IntegerField()

	def __str__(self):
		return "%s,%s,%s,%s"%(self.studyhall, 
			self.date, 
			self.value,
		 	self.desc)

class Course(NameModel):
	# name = models.CharField(max_length=250)

	def __str__(self):
		return self.name
class Student(NameModel):
	# name=models.CharField(max_length=250)
	address = models.TextField(max_length=250)
	phone = models.CharField(max_length=10)
	email = models.CharField(max_length=250)

	def __str__(self):
		return self.name


class Enquiry(NameModel):
	# name = models.CharField(max_length=250)
	course = models.ForeignKey(Course)
	student = models.ForeignKey(Student)
	def __str__(self):
		return "%s,%s,%s"%(self.name,self.student,self.course)

class UserProfile(User):
	# this is inherited model
	# It will create app1_UserProfile table in database
	# There are 2 columns role,user(one to one relation with User model)	
	roles=[('stud', 'student'),('studspace',('studyspace'))]
	role = models.CharField(choices=roles, max_length=2)


# class StudyHall(models.Model):
# 	name = models.CharField(max_length=50)
# 	area = models.TextField(max_length=250)
# 	def __str__(self):
# 		return "%s|%s"%(self.name, self.area)

# class Expenses(models.Model):
# 	studyhall = models.ForeignKey(StudyHall)
# 	date = models.DateTimeField()
# 	name=models.CharField(max_length=250)
# 	desc = models.TextField(max_length=250)
# 	value= models.IntegerField()

# 	def __str__(self):
# 		return "%s,%s,%s,%s"%(self.studyhall, 
# 			self.date, 
# 			self.value,
# 		 	self.desc)

# class Course(models.Model):
# 	name = models.CharField(max_length=250)

# 	def __str__(self):
# 		return self.name
# class Student(models.Model):
# 	name=models.CharField(max_length=250)
# 	address = models.TextField(max_length=250)
# 	phone = models.CharField(max_length=10)
# 	email = models.CharField(max_length=250)

# 	def __str__(self):
# 		return self.name


# class Enquiry(models.Model):
# 	name = models.CharField(max_length=250)
# 	course = models.ForeignKey(Course)
# 	student = models.ForeignKey(Student)
# 	def __str__(self):
# 		return "%s,%s,%s"%(self.name,self.student,self.course)





	

