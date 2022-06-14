from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "created", "updated", "name")
    list_filter = ("created", "updated")
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created",
        "updated",
        "category",
        "color",
        "model",
        "reg_no",
    )
    list_filter = ("created", "updated", "category")
