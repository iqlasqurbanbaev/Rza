from django.contrib import admin
from .models import *

@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
    list_display = ['id','first_name']
    ordering = ['-id']
    search_fields = ['first_name']
admin.site.register(Product )
admin.site.register(Category)

    