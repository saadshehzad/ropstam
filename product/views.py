from django.views.generic import TemplateView
from django.shortcuts import redirect, render, get_object_or_404
 
from .models import Category, Product
from .forms import CategoryForm, ProductForm



class HomePageView(TemplateView):
    template_name = "home.html"


def category_list(request):
    context = {}
    context["dataset"] = Category.objects.all()
    return render(request, "category_list.html", context)

def get_category_by_id(request, id):
    context ={}
    context["data"] = Category.objects.get(id=id)
    return render(request, "category_detail.html", context)

 
def create_category(request):
    context ={}
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("category_list")

    context['form']= form
    return render(request, "create_category.html", context)


def update_category(request, id):
    context ={}
    obj = get_object_or_404(Category, id=id)
    form = CategoryForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("category_list")

    context["form"] = form
    return render(request, "update_category.html", context)


def delete_category(request, id):
    context ={}
    obj = get_object_or_404(Category, id=id)
    if request.method =="POST":
        obj.delete()
        return redirect("category_list")
 
    return render(request, "delete_category.html", context)