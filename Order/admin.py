from django.contrib import admin

from .models import Plate, Menu

@admin.register(Plate)
class PlateAdmin(admin.ModelAdmin):
    pass

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    pass