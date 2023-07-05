from django.contrib import admin
from .models import Discount
# Register your models here.

class DiscountAdmin(admin.ModelAdmin):
    list_display = ("products","code_discount","percentage","expiry_date","minimum_purchase")
admin.site.register(Discount,DiscountAdmin)