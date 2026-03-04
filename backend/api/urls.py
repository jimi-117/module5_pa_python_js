from django.urls import path
from . import views

# Set app_name if you want to use namespacing like 'api:recipes'
# app_name = 'api' 

urlpatterns = [
    path('', views.recipes, name='recipes'),
    path('delete-recipe/<int:id>/', views.delete_recipe, name='delete_recipe'),
    path('update-recipe/<int:id>/', views.update_recipe, name='update_recipe'),
]