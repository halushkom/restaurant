from django.contrib import admin
from order.models import Order

admin.site.register(Order)
class Order(admin.ModelAdmin):
    list_display = ('Name', 'PhoneNumber', 'Choice', 'Data', 'Time')
    list_filter = ('Choice', 'Data')
    #search_fields = ('Name', 'Second_Name', 'PhoneNumber')