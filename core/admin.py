from django.contrib import admin
from .models import Employee, Meal

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'registration_id',
        'department',
        'active',
        'register_date'
    )

    search_fields = (
        'name',
        'registration_id',
    )

    list_filter = (
        'department',
        'active',
    )

    ordering = (
        'name',
    )

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = (
        'employee',
        'meal_date',
        'meal_time',
    )

    search_fields = (
        'employee_name',
        'employee_registration_id',
    )

    list_filter = (
        'meal_date',
        'meal_time',
    )

    date_hierarchy = 'meal_date'
