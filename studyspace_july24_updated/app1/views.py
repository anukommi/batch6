# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from app1.models import StudyHall, Expenses, Enquiry,\
Course, Student, Expenses, UserProfile
from django.contrib.auth import authenticate, login,logout
# \ : it tells python that it is not end of the line
# Create your views here.

def view_index(request):
	# import pdb;pdb.set_trace();
	if request.method=="POST":
		data = request.POST

		if data.get("reg"):
			up = UserProfile.objects.create_user(
				username=data.get("username"),
				password=data.get("password"),
				email = data.get("email")
				)
			return render(request,"app1/index.html",
				{"msg":"USER created successfully!!. Please login"})

		else:
			user=authenticate(
				username=data.get("username"),
				password=data.get("password")
				)
			if user:
				# import pdb;pdb.set_trace()
				# request.session.update({"user":user.username})
				login(request, user)#It requests for session, login in imported
				return render(request, "app1/home.html",
					{"msg": "Login successfully."})
			else:
				return render(request, "app1/home.html",
					{"msg": "Login failed."})

	return render(request,"app1/index.html")

def login_req(f, *args1):
	def inner(*args):
		# if "user" in args[0].session:
		if "_auth_user_id" in args[0].session:
			return f(*args)
		else:
			return redirect(view_index)
	return inner

@login_req
def view_syudyhalls(request):
	# if "user" in request.session:
		if request.method == "POST":
			data=request.POST
			hall =StudyHall(name=data.get("hall_name"),
				area=data.get("hall_area"))
			hall.save()
		studyhalls = StudyHall.objects.all()
		return render(request,"app1/studyhalls.html",{"halls":studyhalls})
	# else:
	# 	return redirect(view_index)	

def view_logout(request):
	if request.method == "POST":
		# request.session.clear()
		logout(request)#imported
		return redirect(view_index)
	return render(request, "app1/logout.html")


def view_hall_update(request,pk):
	hall =StudyHall.objects.get(pk=pk)
	if request.method=="POST":
		data =request.POST
		hall.name=data.get("hall_name")
		hall.area=data.get("hall_area")
		hall.save()
		return redirect(view_syudyhalls)

	return render(request,"app1/hall_update.html",{"data":hall})

def view_hall_delete(request,id):
	hall_info=StudyHall.objects.get(pk=id)
	if request.method=="POST":
		hall_info.delete()
		return redirect(view_syudyhalls)
	return render(request, "app1/hall_delete.html",{"hall":hall_info})

def view_enq_update(request,enq_id):
	enquiry = Enquiry.objects.get(pk=enq_id)
	if request.method == "POST":
		data=request.POST
		cour_inst=Enquiry.objects.get(pk=data.get("enq_id"))
		stud_inst=Enquiry.objects.get(name=data.get("enq_student"))
		enquiry.name=data.get("enq_name")
		enquiry.course=cour_inst
		enquiry.student=stud_inst
		enquiry.save()
		return redirect(view_index)
	return render(request, "app1/enq_update.html", {"enq":enquiry})

def view_student_update(request,stud_id):
	stud = Student.objects.get(pk=stud_id)
	if request.method == "POST":
		data=request.POST
		stud.name=data.get("student_name")
		stud.address=data.get("student_address")
		stud.phone=data.get("student_phone")
		stud.email=data.get("student_email")
		stud.save()
		return redirect(view_index)
	return render(request,"app1/student_update.html",{"student":stud})

def view_student_delete(request,id):
	student = Student.objects.get(pk=id)
	if request.method == "POST":
		student.delete()
		return redirect(view_index)
	return render(request,"app1/student_delete.html",{"stud":student})




# def view_index(request):
# 	if request.method=="POST":
# 		data = request.POST
# 		if data.get("enquiry"):
# 			course_inst = Course.objects.get(pk=data.get("enq_course"))
# 			stdudent_inst = Student.objects.get(pk=data.get("enq_student"))
# 			enq = Enquiry(
# 				name = data.get("enq_name"),
# 				student = stdudent_inst,
# 				course = course_inst
# 				)
# 			enq.save()
# 		elif data.get("expense"):
# 			studyhall_inst = StudyHall.objects.get(pk=data.get("exp_studyhall"))
# 			exp = Expenses(
# 				studyhall = studyhall_inst,
# 				date = data.get("exp_date"),
# 				name = data.get("exp_name"),
# 				desc = data.get("exp_desc"),
# 				value = data.get("exp_value"),
# 				)
# 			exp.save()
# 		# elif data.get("studyhall"):
# 		# 	hall = StudyHall(name=data.get("hall_name"), 
# 		# 		area=data.get("hall_area"))
# 		# 	hall.save()
# 		else:
# 			name=data.get("student_name")
# 			addr=data.get("hall_area")
# 			phn=data.get("phone_num")
# 			email=data.get("email_id")
# 			student_inst=Student(name=name,
# 				address=addr,
# 				phone=phn,
# 				email=email)
# 			student_inst.save()

# 	studyhalls = StudyHall.objects.all()
# 	expenses = Expenses.objects.all()
# 	enquiries = Enquiry.objects.all()
# 	courses = Course.objects.all()
# 	students = Student.objects.all()
# 	return render(request,"app1/index.html",{
# 		"halls": studyhalls,
# 		"exps": expenses,
# 		"enqs": enquiries,
# 		"students": students,
# 		"courses": courses 
# 		})