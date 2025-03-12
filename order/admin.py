from django.contrib import admin
from .models import MenuWeek, MealType, Meal, Order, OrderItem

# Register your models here.

admin.site.register(MealType)
admin.site.register(MenuWeek)


# Adapted use of admin filters from:
# https://mastering-django-admin.avilpage.com/en/latest/admin_filter.html 
class MealAdmin(admin.ModelAdmin):
    list_display = (
        "menu_week",
        "day_of_week",
        "category",
        "name",
        "is_plant_based"
    )
    list_filter = ("menu_week", "category", "day_of_week")
    search_fields = ("name",)


class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "menu_week", "order_date")
    list_filter = ("menu_week", "order_date")
    search_fields = ("user__username",)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "meal", "dietary_notes")
    list_filter = ("meal", "order__menu_week")
    search_fields = ("order__user__username", "meal__name")


admin.site.register(Meal, MealAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
