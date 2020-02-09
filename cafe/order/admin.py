from django.contrib import admin
from order.models import Order

admin.site.register(Order)
#class MakeOrder(admin.ModelAdmin):
    #list_display = ('Name', 'Second_Name', 'PhoneNumber', 'Description')
    #list_filter = ('status', 'created', 'publish', 'author')
    #search_fields = ('Name', 'Second_Name', 'PhoneNumber')