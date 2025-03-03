from django.contrib import admin
from .models import MenuWeek, MealType, Meal, Order, OrderItem

# Register your models here.

admin.site.register(MenuWeek)
admin.site.register(MealType)
admin.site.register(Meal)
admin.site.register(Order)
admin.site.register(OrderItem)