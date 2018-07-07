"""Datacenter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse

'''
def fun(request):
    return HttpResponse("27.56")

'''
from Cooling.views import fun
from Cooling.views import fun1, fun2
from Cooling.views import register_form

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'get_temp', fun),
    url(r'gotohtml', fun1),
    url(r'create_person', register_form),
    url(r'gototemplate', fun2),
]
