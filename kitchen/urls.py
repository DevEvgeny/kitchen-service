from django.urls import path

from .views import (index,
                    DishTypeListView,
                    DishListView,
                    DishDetailView,
                    DishTypeCreateView,
                    DishTypeUpdateView,
                    DishTypeDeleteView,
                    CookListView,
                    CookDetailView)

urlpatterns = [
    path("", index, name="index"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-types-list"),
    path("dish-types/create/", DishTypeCreateView.as_view(), name="dish-types-create"),
    path("dish-types/<int:pk>/update/", DishTypeUpdateView.as_view(), name="dish-types-update"),
    path("dish-types/<int:pk>/delete/", DishTypeDeleteView.as_view(), name="dish-types-delete"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
]

app_name = "kitchen"
