from django.contrib import admin
from .models import Order

# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    # ,를 꼭 써줘야 튜플로 인식해서 문제가 없다.
    list_display = ('user', 'product', 'quantity')


admin.site.register(Order, OrderAdmin)
