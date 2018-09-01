from django.contrib import admin
from .models import Shoes


class ShoesAdmin(admin.ModelAdmin):
    list_display=['id','price','mark','model','numberOfItem','color','sex', 'category']

# Register your models here.
admin.site.register(Shoes, ShoesAdmin)
