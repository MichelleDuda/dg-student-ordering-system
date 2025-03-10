from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import date
from django.utils import timezone
from .models import MenuWeek, Meal, Order, OrderItem

# Views


@login_required
def menu_view(request):
    """Handles retrieving the menu for new oders and updates."""
    today = date.today()
    menu_week = (
        MenuWeek.objects.filter(start_date__gt=today)
        .order_by('start_date')
        .first()
    )

    if not menu_week:
        messages.warning(request, "No menu available for this week.")
        return redirect("past_orders")

    meals_by_day = {
        day: Meal.objects.filter(menu_week=menu_week, day_of_week=day)
        for day in [
            "Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday"
        ]
    }

    # Retrieve user's existing order
    order = Order.objects.filter(
        user=request.user,
        menu_week=menu_week
    ).first()

    # Store user's order in set
    selected_meal_ids = set()
    dietary_notes = {}

    if order:
        for item in order.items.all():
            selected_meal_ids.add(item.meal.id)
            dietary_notes[item.meal.id] = item.dietary_notes or ""

    context = {
        "menu_week": menu_week,
        "meals_by_day": meals_by_day,
        "selected_meal_ids": selected_meal_ids,
        "dietary_notes": dietary_notes if dietary_notes else {},
    }
    return render(request, "order/menu.html", context)


@login_required
def place_order(request):
    """Handles order submission from the menu page."""
    if request.method == "POST":

        menu_week_id = request.POST.get("menu_week_id")
        try:
            menu_week_id = int(menu_week_id)  # Convert to integer
            menu_week = get_object_or_404(MenuWeek, id=menu_week_id)
        except (ValueError, TypeError):
            messages.error(request, "Invalid MenuWeek ID")
            return redirect("menu")

        # Check if an order exists for this user for the week.
        order, created = Order.objects.get_or_create(
            user=request.user,
            menu_week=menu_week
        )

        # Clear preveious selections before updating
        order.items.all().delete()

        for key, meal_id in request.POST.items():
            if key.startswith("meal_"):
                meal = get_object_or_404(Meal, id=meal_id)
                dietary_notes = request.POST.get(f"notes_{meal_id}", "")
                OrderItem.objects.create(
                    order=order,
                    meal=meal,
                    dietary_notes=dietary_notes
                )

        if created:
            messages.success(
                request,
                "Your order has been placed successfully!"
            )
        else:
            messages.success(
                request,
                "Your order has been updated successfully!"
            )

        return redirect("past_orders")

    return redirect("menu")  # Redirect to menu if accessed incorrectly


@login_required
def past_orders(request):
    """Display a user's past orders."""
    orders = Order.objects.filter(user=request.user).order_by("-order_date")

    today = timezone.now().date()
    for order in orders:
        start_date = order.menu_week.start_date

        order.show_buttons = start_date > today
    return render(request, "order/past_orders.html", {"orders": orders})


@login_required
def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if order.user == request.user:
        order.delete()

    return redirect('past_orders')
