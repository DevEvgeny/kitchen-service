from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
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


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-types-list")
    template_name = "kitchen/dish_type_form.html"


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-types-list")
    template_name = "kitchen/dish_type_form.html"


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen:dish-types-list")
    template_name = "kitchen/dish_type_confirm_delete.html"

class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    queryset = Dish.objects.select_related("dish_type")
    paginate_by = 4

class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook