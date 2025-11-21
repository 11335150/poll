from django.contrib import admin
from .models import poll,option #.前面空著代表自己的(default)models.py引用poll跟option
# Register your models here.

admin.site.register(poll)#註冊(register)資源
admin.site.register(option)