from django.contrib import admin
from .models import Category, Product, Post, Order, Address, Appointment
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Post)
admin.site.register(Order)
admin.site.register(Address) 
admin.site.register(Appointment)
