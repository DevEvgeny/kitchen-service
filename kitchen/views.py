from django.shortcuts import render
from django.views import generic

from kitchen.models import (DishType,
                            Dish,
                            Cook)


def index(request):
    """View function for the home page of the site."""
    num_dish_type = DishType.objects.count()
    num_dish = Dish.objects.count()
    num_cooks = Cook.objects.count()

    context = {
        "num_dish_type": num_dish_type,
        "num_dish": num_dish,
        "num_cooks": num_cooks,
    }

    return render(request, "kitchen/index.html", context=context)


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "kitchen/dish_type_list.html"
    context_object_name = "dish_type_list"
    paginate_by = 4


class DishListView(generic.ListView):
    model = Dish
    queryset = Dish.objects.select_related("dish_type")
    paginate_by = 4

class DishDetailView(generic.DetailView):
    model = Dish