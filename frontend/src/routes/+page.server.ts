// frontend/src/routes/+page.server.ts
import type { Actions, PageServerLoad } from './$types';
import type { Recipe } from '$lib/types';
import { fail } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ fetch }) => {
    // get recipes from the backend API Django Rest Framework
    const response = await fetch('http://127.0.0.1:8000/api/');
    
    if (!response.ok) {
        throw new Error(`Failed to fetch recipes: ${response.status}`);
    }

    const recipes: Recipe[] = await response.json();

    return {
        recipes
    };
};

export const actions: Actions = {
    create: async ({ request, fetch }) => {
        const formData = await request.formData();
        const response = await fetch('http://127.0.0.1:8000/api/', {
            method: 'POST',
            body: formData
        });
        
        if (!response.ok) {
            const error = await response.json();
            return fail(response.status, {
                message: error.message || 'Failed to create recipe'
            });
        }
        return { satisfies: true };
    },

    remove: async ({ request, fetch }) => {
        const formData = await request.formData();
        const id = formData.get('id');
        const response = await fetch(`http://127.0.0.1:8000/api/delete-recipe/${id}/`, {
            method: 'DELETE'
        });

        if (!response.ok) {
            return fail(response.status, {
                message: 'Failed to delete recipe'
            });
        }
        return { success: true, message: 'Recipe deleted successfully' };
    },

    update: async ({ request, fetch }) => {
        const formData = await request.formData();
        const id = formData.get('id');
        const response = await fetch(`http://127.0.0.1:8000/api/update-recipe/${id}/`, {
            method: 'PUT',
            body: formData
        });

        if (!response.ok) {
            return fail(response.status, {
                message: 'Failed to update recipe'
            });
        }
        return { success: true, message: 'Recipe updated successfully' };
    }
};
