# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from app1.models import StudyHall
from app1.models import Expense
from app1.models import Enquiry

# Create your views here.
def view_index(request):
	studyhall=StudyHall.objects.all()
	expense=Expense.objects.all()
	enquiry=Enquiry.objects.all()
	return render(request, "app1/index.html",{
		"halls":studyhall,
		"exps":expense,
		"enqs":enquiry,
		})