from django.contrib import admin

# Register your models here.
from closet.models import Closet


# Register your models here.
@admin.register(Closet)
class ClosetAdmin(admin.ModelAdmin):
    list_display = ('classification', 'product_name')
