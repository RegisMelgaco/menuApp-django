from django.contrib import admin

from .models import Plate, Menu, DaySpecial, Order, OrderHasPlate


@admin.register(Plate)
class PlateAdmin(admin.ModelAdmin):
    pass


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    pass


@admin.register(DaySpecial)
class DaySpecialAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderHasPlate)
class OrderHasPlateAdmin(admin.ModelAdmin):
    pass
