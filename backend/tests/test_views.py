from django.urls import reverse
import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from api.models import Recipe

@pytest.mark.django_db
class TestRecipeViews:

    @pytest.fixture
    def sample_recipe(self):
        """Fixture to create a sample recipe for testing."""
        return Recipe.objects.create(
            recipe_name="Test Curry",
            recipe_description="Delicious test curry",
        )

    @pytest.fixture
    def dummy_image(self):
        """Fixture to create a dummy image file in memory."""
        return SimpleUploadedFile(
            name='test_image.jpg',
            content=b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x05\x04\x04\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3b',
            content_type='image/jpeg'
        )

    # 1. Test Listing and Search functionality
    def test_recipes_list_and_search(self, client, sample_recipe):
        # Check if the list view renders correctly
        url = reverse('recipes')
        response = client.get(url)
        assert response.status_code == 200
        assert "Test Curry" in response.content.decode('utf-8')

        # Check search functionality (match found)
        response = client.get(url, {'search': 'Curry'})
        assert "Test Curry" in response.content.decode('utf-8')

        # Check search functionality (no match)
        response = client.get(url, {'search': 'Pasta'})
        assert "Test Curry" not in response.content.decode('utf-8')

    # 2. Test Recipe Creation (POST)
    def test_create_recipe(self, client, dummy_image):
        url = reverse('recipes')
        data = {
            'recipe_name': 'New Recipe',
            'recipe_description': 'New Description',
            'recipe_image': dummy_image
        }
        # Send POST request with multipart data for file upload
        response = client.post(url, data)

        # Should redirect to home page after success
        assert response.status_code == 302
        assert response.url == '/'
        # Verify data is saved in the database
        assert Recipe.objects.filter(recipe_name='New Recipe').exists()

    # 3. Test Recipe Deletion
    def test_delete_recipe(self, client, sample_recipe):
        url = reverse('delete_recipe', kwargs={'id': sample_recipe.id})
        response = client.get(url) # Your view handles deletion via redirect

        assert response.status_code == 302
        assert not Recipe.objects.filter(id=sample_recipe.id).exists()

    # 4. Test Recipe Update (GET and POST)
    def test_update_recipe(self, client, sample_recipe):
        url = reverse('update_recipe', kwargs={'id': sample_recipe.id})
        
        # Verify the update page displays existing data
        response = client.get(url)
        assert response.status_code == 200
        
        # Submit updated data
        updated_data = {
            'recipe_name': 'Updated Name',
            'recipe_description': 'Updated Description',
        }
        response = client.post(url, updated_data)
        
        # Refresh the object from DB and verify changes
        sample_recipe.refresh_from_db()
        assert response.status_code == 302
        assert sample_recipe.recipe_name == 'Updated Name'
        assert sample_recipe.recipe_description == 'Updated Description'