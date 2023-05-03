from django.contrib import admin
from models import Menu
# Register your models here.

class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'url')

admin.site.register(Menu, MenuAdmin)
