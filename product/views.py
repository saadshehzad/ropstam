from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView

from .forms import CategoryForm, ProductForm
from .models import Category, Product


def home(request):
    context = {"products": Product.objects.all()}
    return render(request, "home.html", context)


# CRUD for categories


def category_list(request):
    context = {}
    context["dataset"] = Category.objects.all()
    return render(request, "category_list.html", context)


def get_category_by_id(request, id):
    context = {}
    context["data"] = Category.objects.get(id=id)
    return render(request, "category_detail.html", context)


def create_category(request):
    context = {}
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("category_list")

    context["form"] = form
    return render(request, "create_category.html", context)


def update_category(request, id):
    context = {}
    obj = get_object_or_404(Category, id=id)
    form = CategoryForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("category_list")

    context["form"] = form
    return render(request, "update_category.html", context)


def delete_category(request, id):
    context = {}
    obj = get_object_or_404(Category, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect("category_list")

    return render(request, "delete_category.html", context)


# CRUD for products


def product_list(request):
    context = {}
    context["dataset"] = Product.objects.all()
    return render(request, "product_list.html", context)


def get_product_by_id(request, id):
    context = {}
    context["data"] = Product.objects.get(id=id)
    return render(request, "product_detail.html", context)


def create_product(request):
    context = {}
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("product_list")

    context["form"] = form
    return render(request, "create_product.html", context)


def update_product(request, id):
    context = {}
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("product_list")

    context["form"] = form
    return render(request, "update_product.html", context)


def delete_product(request, id):
    context = {}
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect("product_list")

    return render(request, "delete_product.html", context)
