# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def fun_purchase(request):
	return render(request, "purchase/index.html")