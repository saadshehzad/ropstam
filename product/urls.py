from django.urls import path

from .views import *

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("categories/", category_list, name="category_list"),
    path("create/category/", create_category, name="create_category"),
    path("categories/<int:id>/", get_category_by_id, name="get_category_by_id"),
    path("categories/<int:id>/update/", update_category, name="update_category"),
    path("categories/<int:id>/delete/", delete_category, name="delete_category"),

    path("products/", product_list, name="product_list"),
    path("create/product/", create_product, name="create_product"),
    path("products/<int:id>/", get_product_by_id, name="get_product_by_id"),
    path("products/<int:id>/update/", update_product, name="update_product"),
    path("products/<int:id>/delete/", delete_product, name="delete_product")
]
