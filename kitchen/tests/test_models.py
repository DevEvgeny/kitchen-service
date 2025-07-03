from django.contrib.auth import get_user_model
from django.test import TestCase

from kitchen.models import DishType, Dish


class ModelTest(TestCase):
    def test_dish_type_str(self):
        dish_type = DishType.objects.create(
            name="test"
        )
        self.assertEqual(str(dish_type), dish_type.name)

    def test_cook_str(self):
        cook = get_user_model().objects.create(
            username="test",
            password="test1234",
            first_name="testfirstname",
            last_name="testlastname"
        )
        self.assertEqual(str(cook), f"{cook.username} {cook.first_name} {cook.last_name}")

    def test_create_cook_with_year_of_experience(self):
        username = "test"
        password = "test1234"
        year_of_experience = "2"
        cook = get_user_model().objects.create_user(
            username=username,
            password=password,
            year_of_experience=year_of_experience
        )
        self.assertEqual(cook.username, username)
        self.assertTrue(cook.password, password)
        self.assertEqual(cook.year_of_experience, year_of_experience)

    def test_dish_str(self):
        dish_type = DishType.objects.create(
            name="test"
        )
        dish = Dish.objects.create(
            name="test",
            price="10.55",
            dish_type=dish_type
        )
        self.assertEqual(str(dish), f"{dish.name} {dish.dish_type} {dish.price}")