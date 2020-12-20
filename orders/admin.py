from django.contrib import admin

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user','order_type','amount','ref_number','completed','date_created')
    list_filter = ('order_type', 'completed')
    search_fields = ('user', 'ref_number')
    ordering = ('date_created')
