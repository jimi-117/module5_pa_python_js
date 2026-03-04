from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Recipe
from .serializers import RecipeSerializer

@api_view(['GET', 'POST'])
def recipes(request):
    if request.method == 'POST':
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    queryset = Recipe.objects.all()
    search = request.query_params.get('search')
    if search:
        queryset = queryset.filter(recipe_name__icontains=search)

    serializer = RecipeSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    recipe.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def update_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    
    if request.method == 'POST':
        serializer = RecipeSerializer(recipe, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer = RecipeSerializer(recipe)
    return Response(serializer.data)
