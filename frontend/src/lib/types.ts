// Determine the types for the recipe obj from Django Rest Framework backend.
// So that we use snake case for the keys.

export interface Recipe{
    id: number;
    recipe_name: string;
    recipe_description: string;
    recipe_image: string | null;
    created_at?: string;
    updated_at?: string;    
}