from django.contrib import admin
from .models import Flavor, Size, Topping,Customer, Order, Pizza, Bread

mymodels=[Flavor, Size, Topping,Customer,Order,Pizza,Bread]
admin.site.register(mymodels)
# Register your models here.
