from django.contrib import admin
from .models import Order, Order_item, Vendor

class ItemInLine(admin.TabularInline):
    model = Order_item
    extra = 2

class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Date',            {'fields': ['order_date', 'order_is_complete']}),
        ('Contact Info',    {'fields': ['order_contact_name','order_contact_phone','order_contact_email']})
    ]
    inlines = [ItemInLine]
    list_display = ('order_date', 'order_contact_name')
    list_filter = ['order_is_complete']
    search_fields = ['order_contact_name']

admin.site.register(Order, OrderAdmin)
admin.site.register(Vendor)