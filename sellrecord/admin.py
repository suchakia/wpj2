from django.contrib import admin
from .models import Sellrecord

admin.site.site_header = 'Waaneiza Sellrecord Managment System'

class SellrecordAdmin(admin.ModelAdmin):
	list_display = ['date','customer_name' , 'customer_phone' , 'price' , 'showroom' , 'paid','purchased_item']
	list_filter = ['date','customer_name' , 'customer_phone' , 'price' , 'showroom' , 'paid','purchased_item']
	search_fields = ['date','customer_name' , 'customer_phone' , 'price' , 'showroom' , 'paid','purchased_item']
  	
admin.site.register(Sellrecord, SellrecordAdmin)
