from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import date
from .models import MenuWeek, Meal, Order, OrderItem

# Views

def index(request):
   return render(request, 'menu/index.html')

@login_required  # Ensures users can only access if logged in
def menu_view(request):
   today = date.today()
   menu_week = MenuWeek.objects.filter(start_date__lte=today).order_by('-start_date').first()

   if not menu_week:
        messages.warning(request, "No menu available for this week.")
        return redirect("past_orders")
    
   meals_by_day = {day: Meal.objects.filter(menu_week=menu_week, day_of_week=day) for day in 
        ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]}

   context = {"menu_week": menu_week, "meals_by_day": meals_by_day}
   return render(request, "menu.html", context)


@login_required # Ensures users can only access if logged in
def place_order(request):
    """Handles order submission from the menu page."""
    if request.method == "POST":
        menu_week_id = request.POST.get("menu_week")
        menu_week = get_object_or_404(MenuWeek, id=menu_week_id)

        for key, meal_id in request.POST.items():
            if key.startswith("meal_"):  
                meal = get_object_or_404(Meal, id=meal_id)
                dietary_notes = request.POST.get(f"notes_{meal_id}", "")
                OrderItem.objects.create(order=order, meal=meal, dietary_notes=dietary_notes)

        messages.success(request, "Your order has been placed successfully!")
        return redirect("past_orders")  
    
    return redirect("menu")  # Redirect to menu if accessed incorrectly

@login_required # Ensures users can only access if logged in
def past_orders(request):
    """Display a user's past orders."""
    orders = Order.objects.filter(user=request.user).order_by("-order_date")
    return render(request, "order/past_orders.html", {"orders": orders})