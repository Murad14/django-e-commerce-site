from django.contrib import admin
from .models import Products, Order
# Register your models here.

admin.site.site_header = "E-commerce site"
admin.site.site_title = "Shopno"
admin.site.index_title = "Manage Shopping"

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','price','discount_price','category','description')
    

admin.site.register(Products,ProductAdmin)
admin.site.register(Order)