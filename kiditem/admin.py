from django.contrib import admin
from .models import Category, Product, Post, Order, Appointment, Address
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Post)
admin.site.register(Order)
admin.site.register(Appointment)
admin.site.register(Address)
