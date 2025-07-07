from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from kitchen.models import Cook, Dish, DishType


@admin.register(Cook)
class CookAdmin(UserAdmin):
    fieldsets = list(UserAdmin.fieldsets)
    list_display = UserAdmin.list_display + ("year_of_experience",)

    for i, (name, section) in enumerate(fieldsets):
        if name == "Personal info":
            section["fields"] = section["fields"] + ("year_of_experience",)
            fieldsets[i] = (name, section)
            break


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ["name",
                    "price",
                    "dish_type",
                    # "get_cooks",
                    ]

    # def get_cooks(self, obj):
    #     return ", ".join([str(cook) for cook in obj.cooks.all()])
    #
    # get_cooks.short_description = "Cooks"


admin.site.unregister(Group)
admin.site.register(DishType)
