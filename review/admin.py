from django.contrib import admin
from .models import Review
# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    list_display = ("product","user_id","product_id","ratings","comments")
admin.site.register(Review,ReviewAdmin)