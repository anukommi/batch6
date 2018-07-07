# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def fun_sales(request):
	return render(request, "sales/index.html")