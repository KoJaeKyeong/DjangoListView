from django.contrib import admin
from mypick.models import Mypick


# Register your models here.
@admin.register(Mypick)
class MypickAdmin(admin.ModelAdmin):
    list_display = ('id', 'top_product_name', 'pants_product_name')
