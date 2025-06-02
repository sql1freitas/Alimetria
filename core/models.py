from django.db import models
from django.utils import timezone

class Employee(models.Model):

    name = models.CharField(blank=False,
                            null=False,
                            max_length=255,
                            verbose_name="Nome do Funcionário: ")
    
    registration_id = models.CharField(blank=False,
                                 null=False,
                                 max_length=255,
                                 unique=True,
                                 verbose_name="Matrícula")
    
    department = models.CharField(blank=True,
                                  null=True,
                                  max_length=255,
                                  verbose_name="Setor")
    
    active = models.BooleanField(blank=False,
                                 null=False,
                                 verbose_name="Funcionário Ativo")
    
    register_date = models.DateTimeField(auto_now_add=True,
                                         verbose_name="Data de registro")
    
    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"

    def __str__(self):
        return f"{self.name} ({self.registration_id})"
    

class Meal(models.Model):

    employee = models.ForeignKey('Employee', on_delete=models.CASCADE,
                                 blank=False,
                                 null=False,
                                 verbose_name="Funcionário")
    
    meal_date = models.DateField(default= timezone.now,
                                    verbose_name="Data da refeição")
    
    meal_time = models.TimeField(auto_now_add=True,
                                 verbose_name="Hora da refeição")
                                  
    
    class Meta:
        verbose_name = "Refeição"
        verbose_name_plural = "Refeições"
        constraints =[
            models.UniqueConstraint(fields=['employee', 'meal_date'], name= 'unique_meal_per_employee')
        ]
    
    def __str__(self):
        return f"{self.employee.name} - {self.meal_date}"

