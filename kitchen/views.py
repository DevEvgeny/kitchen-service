from django.shortcuts import render

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