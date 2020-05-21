from django.contrib import admin
from order.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ['Name', 'PhoneNumber', 'Choice', 'Date', 'Time', 'Mail']
    list_filter = ('Choice', 'Date')
    search_fields = ('Name', 'Second_Name', 'PhoneNumber')

admin.site.register(Order, OrderAdmin)