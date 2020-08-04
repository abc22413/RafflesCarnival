from django.contrib import admin
from .models import *

class CouponAdmin(admin.ModelAdmin):
    list_display = (
        'coupon_id', 
        'active', 
        'updated_at'
    )
    list_filter = (
        'active', 
        'updated_at'
    )
    search_fields = (
        'coupon_id',
    )

# Register your models here.
admin.site.register(Coupon, CouponAdmin)