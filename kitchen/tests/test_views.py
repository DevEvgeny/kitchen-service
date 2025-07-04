from http.client import responses

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import DishType, Dish

DISH_TYPE_URL = reverse("kitchen:dish-types-list")
DISH_URL = reverse("kitchen:dish-list")
COOK_URL = reverse("kitchen:cook-list")
INDEX_URL = reverse("kitchen:index")


class PublicTestView(TestCase):
    def test_index_login_required(self):
        res = self.client.get(INDEX_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_dish_type_login_required(self):
        res = self.client.get(DISH_TYPE_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_dish_login_required(self):
        res = self.client.get(DISH_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_cook_login_required(self):
        res = self.client.get(COOK_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test1234"
        )
        self.client.force_login(self.user)

    def test_retrieve_dish_type(self):
        DishType.objects.create(
            name="test"
        )
        DishType.objects.create(
            name="test1"
        )
        dish_type = DishType.objects.all()
        response = self.client.get(DISH_TYPE_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["dish_type_list"]), list(dish_type)
        )
        self.assertTemplateUsed(response, "kitchen/dish_type_list.html")

    def test_retrieve_dish(self):
        dish_type = DishType.objects.create(
            name="test"
        )
        Dish.objects.create(
            name="test",
            price="10.55",
            dish_type=dish_type
        )
        Dish.objects.create(
            name="test1",
            price="10.59",
            dish_type=dish_type
        )
        dish = Dish.objects.all()
        response = self.client.get(DISH_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["dish_list"]), list(dish))
        self.assertTemplateUsed(response, "kitchen/dish_list.html")

    def test_retrieve_cook_list(self):
        get_user_model().objects.create_user(
            username="testes",
            password="test1234",
            year_of_experience="1"
        )
        get_user_model().objects.create_user(
            username="teste",
            password="test12345",
            year_of_experience="2"
        )
        user = get_user_model().objects.all()
        response = self.client.get(COOK_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["cook_list"]), list(user))
        self.assertTemplateUsed(response, "kitchen/cook_list.html")