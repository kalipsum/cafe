from django.contrib import admin
from orders.models import OrderStatus,Order
# Register your models here.
admin.site.register(OrderStatus)
admin.site.register(Order)