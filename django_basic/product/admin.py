from django.contrib import admin
from .models import Product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    # ,를 꼭 써줘야 튜플로 인식해서 문제가 없다.
    list_display=('name','price')
    
admin.site.register(Product, ProductAdmin)