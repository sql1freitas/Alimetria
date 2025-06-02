from django.test import TestCase

from django.test import TestCase
from django.utils import timezone
from .models import Employee, Meal

class MealTestCase(TestCase):

    def setUp(self):
        self.emp = Employee.objects.create(
            name="João Teste",
            registration_id="12345"
        )

    def test_meal_registration(self):
        meal = Meal.objects.create(employee=self.emp)
        self.assertEqual(meal.employee.name, "João Teste")

    def test_unique_meal_per_day(self):
        Meal.objects.create(employee=self.emp, meal_date=timezone.now().date())
        with self.assertRaises(Exception):
            Meal.objects.create(employee=self.emp, meal_date=timezone.now().date())

