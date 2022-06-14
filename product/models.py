from django.db import models
from .utils import TimeStampedModel

class Category(TimeStampedModel, models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(TimeStampedModel, models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categories")
    color = models.CharField(max_length=100)
    model = models.IntegerField()
    reg_no = models.CharField(max_length=100)

    def __str__(self):
        return self.name