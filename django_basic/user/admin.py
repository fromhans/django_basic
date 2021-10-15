from django.contrib import admin
from .models import User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    # ,를 꼭 써줘야 튜플로 인식해서 문제가 없다.
    list_display = ('email', 'level')


admin.site.register(User, UserAdmin)
