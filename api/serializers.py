import random

from django.contrib.auth import get_user_model
from rest_framework import serializers

from product.models import Category, Product

User = get_user_model()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(read_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=str(random.randint(1, 10)),
        )
        return user

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "password",
        )
