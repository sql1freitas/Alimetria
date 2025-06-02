from django.shortcuts import render
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Meal, Employee

def register_meal(request):
    if request.method == 'POST':
        reg_id = request.POST.get('registration_id')
        try:
            employee = Employee.objects.get(registration_id=reg_id, active=True)
        except Employee.DoesNotExist:
            messages.error(request, "Matrícula não encontrada ou funcionário inativo.")
            return redirect('register_meal')

        try:
            Meal.objects.create(employee=employee)
            messages.success(request, "Refeição registrada com sucesso!")
        except IntegrityError:
            messages.warning(request, "Este funcionário já registrou refeição hoje.")
        
        return redirect('register_meal')

    return render(request, 'register_meal.html')

