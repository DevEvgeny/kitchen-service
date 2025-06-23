from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from kitchen.models import Cook, Dish, DishType


# @admin.register(Cook)
# class CookAdmin(UserAdmin):
#     list_display = UserAdmin.list_display + ("year_of_experience", )
#     fieldsets = UserAdmin.fieldsets + (
#         (("Personal info", {"fields": ("year_of_experience",)}),)
#     )
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
                    ]


admin.site.unregister(Group)
admin.site.register(DishType)
