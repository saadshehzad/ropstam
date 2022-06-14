from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from django.contrib.auth import get_user_model
from product.models import Category, Product
from .serializers import CategorySerializer, ProductSerializer, UserSerializer
from rest_framework import permissions
from django.core.mail import send_mail

User = get_user_model()

class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = [permissions.AllowAny,]
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        send_mail(
            'Thanks for registring',
            'Here is the message.',
            'ropstan@abc.com',
            [request.user],
            fail_silently=False,
        )
        return self.create(request, *args, **kwargs)


class CategoryListView(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class ProductListView(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ProductDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()