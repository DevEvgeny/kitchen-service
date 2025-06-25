from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from kitchen.models import (DishType,
                            Dish,
                            Cook)


@login_required
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


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    template_name = "kitchen/dish_type_list.html"
    context_object_name = "dish_type_list"
    paginate_by = 4


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    queryset = Dish.objects.select_related("dish_type")
    paginate_by = 4

class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish