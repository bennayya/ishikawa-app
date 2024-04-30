# serializers.py
from rest_framework import serializers
from .models import IshikawaDiagram, Category, Cause

class CauseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cause
        fields = ['description']

class CategorySerializer(serializers.ModelSerializer):
    causes = CauseSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['name', 'causes']

class IshikawaDiagramSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = IshikawaDiagram
        fields = ['title', 'created_at', 'categories']
