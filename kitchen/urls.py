from django.urls import path

from .views import (index,
                    DishTypeListView,
                    DishListView,
                    DishDetailView,
                    DishCreateView,
                    DishUpdateView,
                    DishDeleteView,
                    DishTypeCreateView,
                    DishTypeUpdateView,
                    DishTypeDeleteView,
                    CookListView,
                    CookDetailView,
                    CookCreateView,
                    CookDeleteView,
                    CookUpdateView)

urlpatterns = [
    path("", index, name="index"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-types-list"),
    path("dish-types/create/", DishTypeCreateView.as_view(), name="dish-types-create"),
    path("dish-types/<int:pk>/update/", DishTypeUpdateView.as_view(), name="dish-types-update"),
    path("dish-types/<int:pk>/delete/", DishTypeDeleteView.as_view(), name="dish-types-delete"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("dishes/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("dishes/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("cooks/create/", CookCreateView.as_view(), name="cook-create"),
    path("cooks/<int:pk>/delete/", CookDeleteView.as_view(), name="cook-delete"),
    path("cooks/<int:pk>/update/", CookUpdateView.as_view(), name="cook-update"),
]

app_name = "kitchen"
