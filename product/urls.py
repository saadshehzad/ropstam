from django.urls import path

from api.views import *

from .views import *

urlpatterns = [
    path("", home, name="home"),
    # Category URLS
    path("categories/", category_list, name="category_list"),
    path("create/category/", create_category, name="create_category"),
    path("categories/<int:id>/", get_category_by_id, name="get_category_by_id"),
    path("categories/<int:id>/update/", update_category, name="update_category"),
    path("categories/<int:id>/delete/", delete_category, name="delete_category"),
    # Product URLS
    path("products/", product_list, name="product_list"),
    path("create/product/", create_product, name="create_product"),
    path("products/<int:id>/", get_product_by_id, name="get_product_by_id"),
    path("products/<int:id>/update/", update_product, name="update_product"),
    path("products/<int:id>/delete/", delete_product, name="delete_product"),
    # API URLS
    path("api/auth/register/", CreateUserView.as_view()),
    path("api/categories/", CategoryListView.as_view()),
    path("api/categories/<int:pk>/", CategoryDetailView.as_view()),
    path("api/products/", ProductListView.as_view()),
    path("api/products/<int:pk>/", ProductDetailView.as_view()),
]
