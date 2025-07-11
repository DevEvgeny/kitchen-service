from django.contrib.admin.templatetags.admin_list import search_form
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kitchen.forms import CookCreationForm, DishForm, SearchForm, CookUpdateForm
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

    def get_context_data(
        self, *, object_list = ..., **kwargs
    ):
        context = super(DishTypeListView, self).get_context_data(**kwargs)
        param = self.request.GET.get("param", "")
        context["search_form"] = SearchForm(
            initial={"param": param}
        )
        return context

    def get_queryset(self):
        form = SearchForm(self.request.GET)
        queryset = DishType.objects.all()

        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["param"]
            )
        return queryset

class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-types-list")
    template_name = "kitchen/dish_type_form.html"


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
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

    def get_context_data(
        self, *, object_list = ..., **kwargs
    ):
        context = super(DishListView, self).get_context_data(**kwargs)
        param = self.request.GET.get("param", "")
        context["search_form"] = SearchForm(
            initial={"param": param}
        )
        return context

    def get_queryset(self):
        form = SearchForm(self.request.GET)
        queryset = Dish.objects.select_related("dish_type")

        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["param"]
            )
        return queryset

class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    form_class = DishForm


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("kitchen:dish-list")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    paginate_by = 5

    def get_context_data(
        self, *, object_list = ..., **kwargs
    ):
        context = super(CookListView, self).get_context_data(**kwargs)
        param = self.request.GET.get("param", "")
        context["search_form"] = SearchForm(
            initial={"param": param}
        )
        return context

    def get_queryset(self):
        form = SearchForm(self.request.GET)
        queryset = Cook.objects.order_by("id")

        if form.is_valid():
            return queryset.filter(
                username__icontains=form.cleaned_data["param"],
            )
        return queryset

class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookCreationForm
    success_url = reverse_lazy("kitchen:cook-list")


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("kitchen:cook-list")


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    form_class = CookUpdateForm
    success_url = reverse_lazy("kitchen:cook-detail")



