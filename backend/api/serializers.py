from rest_framework import serializers
from .models import Recipe


class RecipeSerializer(serializers.ModelSerializer[Recipe]):
    class Meta:
        model = Recipe
        fields = "__all__"
