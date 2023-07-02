from django.contrib import admin
from .models import Products, Order
# Register your models here.

admin.site.site_header = "E-commerce site"
admin.site.site_title = "Shopno"
admin.site.index_title = "Manage Shopping"



class ProductAdmin(admin.ModelAdmin):
    
    def change_catgory_to_default(self,req,queryset):
        queryset.update(category="default")
        
    change_catgory_to_default.short_description ='Default Category'
    list_display = ('title','price','discount_price','category','description')
    search_fields = ['title','category','price','discount_price']
    actions = ('change_catgory_to_default',)
    fields = ('title','price',)
    list_editable = ('price','category',)
    
    
    

admin.site.register(Products,ProductAdmin)
admin.site.register(Order)