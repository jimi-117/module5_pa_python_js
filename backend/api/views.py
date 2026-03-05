from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db.models import QuerySet
from .models import Recipe
from .serializers import RecipeSerializer


@api_view(["GET", "POST"])
def recipes(request: Request) -> Response:
    """
    Handle GET and POST requests for recipes.

    GET: Retrieve all recipes with optional search filtering by recipe name.
        Query Parameters:
            search (str, optional): Filter recipes by name (case-insensitive).
        Returns:
            Response: List of serialized recipe objects.

    POST: Create a new recipe.
         Request Body:
            JSON object containing recipe data.
         Returns:
            Response: Serialized recipe data with HTTP 201 CREATED status on success,
                    or error details with HTTP 400 BAD REQUEST status on validation failure.
    """
    """"""
    if request.method == "POST":
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    queryset: QuerySet[Recipe] = Recipe.objects.all()

    search: str | None = request.query_params.get("search")
    if search:
        queryset = queryset.filter(recipe_name__icontains=search)

    serializer = RecipeSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(["DELETE"])
def delete_recipe(request: Request, id: int) -> Response:
    """Handle DELETE request to delete a recipe by ID.
    Args:
        - request (Request): The incoming HTTP request.
        - id (int): The ID of the recipe to be deleted.
    Returns:
        - Response: HTTP 204 NO CONTENT status on successful deletion,
          or HTTP 404 NOT FOUND if the recipe does not exist.
    """
    recipe: Recipe = get_object_or_404(Recipe, id=id)
    recipe.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "PATCH", "PUT"])
def update_recipe(request: Request, id: int) -> Response:
    """Handle GET, PATCH, and PUT requests to retrieve or update a recipe by ID.
    Args:
        - request (Request): The incoming HTTP request.
        - id (int): The ID of the recipe to be retrieved or updated.
    Returns:
        - Response: For GET, returns serialized recipe data with HTTP 200 OK status.
        - For PATCH/PUT, returns serialized updated recipe data with HTTP 200 OK status on success,
          or error details with HTTP 400 BAD REQUEST status on validation failure.
    """
    recipe: Recipe = get_object_or_404(Recipe, id=id)

    if request.method in ["PATCH", "PUT"]:
        serializer = RecipeSerializer(recipe, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer = RecipeSerializer(recipe)
    return Response(serializer.data)
