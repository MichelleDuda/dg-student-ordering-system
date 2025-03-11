"""
URL configuration for dj_ordering_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from menu import views as menu_views
from about import views as about_views
from order import views as order_views

urlpatterns = [
    path('', menu_views.index, name='home'),
    path('about/', about_views.about, name='about'),
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path(
        'create_menu_week/',
        order_views.create_new_menu,
        name='create_new_menu'
    ),
    path(
        'delete_order/<int:order_id>/',
        order_views.delete_order,
        name='delete_order'
    ),
    path('sample_menu/', about_views.sample_menu, name='sample_menu'),
    path('student_dashboard/', menu_views.dashboard, name='student_dashboard'),
    path("menu/", order_views.menu_view, name="menu"),
    path("place_order/", order_views.place_order, name="place_order"),
    path("past_orders/", order_views.past_orders, name="past_orders"),
    path('update_profile/', menu_views.update_profile, name='update_profile')
]

handler404 = 'menu.views.handler404'
handler500 = 'menu.views.handler500'
