from django.contrib import admin
from .models import MenuWeek, MealType, Meal, Order, OrderItem

# Register your models here.

admin.site.register(MenuWeek)
admin.site.register(MealType)
admin.site.register(Order)
admin.site.register(OrderItem)


class MealAdmin(admin.ModelAdmin):
    list_display = (
        "menu_week",
        "day_of_week",
        "category",
        "name",
        "is_plant_based"
    )
    list_filter = ("menu_week", "category", "day_of_week")


admin.site.register(Meal, MealAdmin)
