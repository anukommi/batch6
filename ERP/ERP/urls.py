"""ERP URL Configuration

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

from product.views import fun_product
from warehouse.views import fun_warehouse
from stock.views import fun_stock
from sales.views import fun_sales
from purchase.views import fun_purchase

def fun(request):
    #return "Hello Django"
    #return HttpResponse("Hello Djano")
    return HttpResponse("<h1>Hello Django</h1>")

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'request_url', fun),
    url(r'products', fun_product),
    url(r'warehouse', fun_warehouse),
    url(r'stock', fun_stock),
    url(r'sales', fun_sales),
    url(r'purchase', fun_purchase),
]




    







