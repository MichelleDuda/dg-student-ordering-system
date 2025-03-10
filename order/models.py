from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class MenuWeek(models.Model):
    """Defines each weekly menu cycle by start date"""
    start_date = models.DateField(
        unique=True,
        help_text="Start date of this week's menu"
    )

    def __str__(self):
        return f"Menu for week beginning {self.start_date}"


class MealType(models.Model):
    meal_type = models.CharField(
        max_length=10,
        choices=[
            ("Breakfast", "Breakfast"),
            ("Lunch", "Lunch"),
            ("Dinner", "Dinner")]
    )

    def __str__(self):
        return self.meal_type


class Meal(models.Model):
    menu_week = models.ForeignKey(
        MenuWeek,
        on_delete=models.CASCADE,
        related_name="meals"
    )
    day_of_week = models.CharField(
        max_length=10,
        choices=[
            ("Monday", "Monday"),
            ("Tuesday", "Tuesday"),
            ("Wednesday", "Wednesday"),
            ("Thursday", "Thursday"),
            ("Friday", "Friday"),
            ("Saturday", "Saturday"),
            ("Sunday", "Sunday"),
        ]
    )
    category = models.ForeignKey(MealType, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    is_plant_based = models.BooleanField(default=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return (
            f"{self.menu_week} - {self.day_of_week} - "
            f"{self.category.meal_type}: {self.name}"
        )


class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="orders"
    )
    menu_week = models.ForeignKey(
        MenuWeek,
        on_delete=models.CASCADE,
        related_name="orders"
    )
    order_date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'menu_week')

    def __str__(self):
        return f"Order by {self.user.username} on ({self.order_date})"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items"
    )
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    dietary_notes = models.TextField(blank=True)

    def __str__(self):
        return (
            f"{self.order.user.username} - {self.meal.name} "
            f"({self.order.order_date})"
        )
