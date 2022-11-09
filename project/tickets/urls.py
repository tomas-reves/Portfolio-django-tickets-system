from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tickets/', views.user_tickets_view, name='tickets'),
    path('add_ticket/', views.add_ticket),
    path('my_tickets/', views.user_my_tickets_view),
    path('assigned_tickets/', views.assigned_tickets_view),
    path('update_ticket/<str:pk>/', views.update_ticket, name='update_ticket'),
    path('delete_ticket/<str:pk>/', views.delete_ticket, name='delete_ticket'),
]
