from django.contrib.auth import get_user_model
from django.test import TestCase

from kitchen.forms import CookCreationForm, CookUpdateForm, SearchForm


class FormTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test1234"
        )

    def test_cook_creation_form(self):
        form_data = {
            "username": "testname",
            "year_of_experience": "5",
            "first_name": "testfirst",
            "last_name": "testlast",
            "password1": "test_785412",
            "password2": "test_785412",
        }
        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_cook_update_form(self):
        form_data = {
            "username": "testname",
            "first_name": "testfirst",
            "last_name": "testlast",
            "year_of_experience": "5"
        }
        form = CookUpdateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_search_form(self):
        form_data = {
            "param": "Test",
        }
        form = SearchForm(data=form_data)
        self.assertTrue(form.is_valid())