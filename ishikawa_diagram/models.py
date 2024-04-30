from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# models.py
from django.db import models

class IshikawaDiagram(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Methods
    def __str__(self):
        return self.title

    def get_categories(self):
        return self.categories.all()

    def get_total_categories(self):
        return self.categories.count()

class Category(models.Model):
    diagram = models.ForeignKey(IshikawaDiagram, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=100)
    # Methods
    def __str__(self):
        return self.name

class Cause(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='causes')
    description = models.TextField()
    # Methods
    def __str__(self):
        return self.description