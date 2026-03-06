<script lang="ts">
    import { enhance } from '$app/forms';
    import type { ActionData, PageData } from './$types';
	let { data, form }: { data: PageData; form: ActionData } = $props();
    let editingId = $state<number | null>(null);
    const DJANGO_URL = 'http://127.0.1:8000/';
</script>

<main style="max-width: 800px; margin: 0 auto; padding: 2rem; font-family: sans-serif; line-height: 1.6;">
	<h1 style="border-bottom: 2px solid #eee; padding-bottom: 0.5rem;">🍳 Django Recipe Manager</h1>

	<section style="background: #f9f9f9; padding: 1.5rem; border-radius: 8px; margin-bottom: 3rem;">
		<h2 style="margin-top: 0;">Create New Recipe</h2>
		
		<form 
			method="POST" 
			action="?/create" 
			use:enhance 
			enctype="multipart/form-data"
			style="display: flex; flex-direction: column; gap: 1rem;"
		>
			<input type="text" name="recipe_name" placeholder="Recipe Name" required style="padding: 0.5rem;" />
			<textarea name="recipe_description" placeholder="Description" rows="3" style="padding: 0.5rem;"></textarea>
			<input type="file" name="recipe_image" accept="image/*" style="font-size: 0.9rem;" />
			
			<button type="submit" style="background: #4CAF50; color: white; border: none; padding: 0.7rem; border-radius: 4px; cursor: pointer; font-weight: bold;">
				Save Recipe
			</button>
		</form>

		{#if form}
			{#if 'success' in form && form.success}
				<p style="color: green; font-weight: bold; margin-top: 1rem;">✅ Recipe created successfully!</p>
			{:else if 'message' in form}
				<p style="color: red; margin-top: 1rem;">❌ {form.message}</p>
			{/if}
		{/if}
	</section>

	<section>
		<h2>Recipe List</h2>
		{#if data.recipes && data.recipes.length > 0}
			<div style="display: grid; gap: 1.5rem; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));">
				{#each data.recipes as recipe}
					<article style="border: 1px solid #ddd; padding: 1rem; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); transition: transform 0.2s;">
                        {#if editingId === recipe.id}
                                <form method="POST" action="?/update" use:enhance={() => {
                                    return async ({ update }) => {
                                        // After successful update, reset editingId to null to exit edit mode
                                        editingId = null;
                                        await update();
                                    };
                                }} enctype="multipart/form-data" style="display: flex; flex-direction: column; gap: 0.5rem;">
                                    <input type="hidden" name="id" value={recipe.id} />
                                    <input type="text" name="recipe_name" value={recipe.recipe_name} required style="padding: 0.3rem;" />
                                    <textarea name="recipe_description" style="padding: 0.3rem;">{recipe.recipe_description}</textarea>
                                    <div style="display: flex; gap: 0.5rem;">
                                        <button type="submit" style="background: #2196F3; color: white; border: none; padding: 0.4rem; border-radius: 4px; flex: 1;">Update</button>
                                        <button type="button" onclick={() => editingId = null} style="background: #ccc; border: none; padding: 0.4rem; border-radius: 4px; flex: 1;">Cancel</button>
                                    </div>
                                </form>
                        {:else}
                            <h3 style="margin-top: 0; color: #333;">{recipe.recipe_name}</h3>
                            <p style="color: #666; font-size: 0.9rem; min-height: 3rem;">{recipe.recipe_description}</p>
                            
                            {#if recipe.recipe_image}
                                <img 
                                    src="{DJANGO_URL}{recipe.recipe_image}" 
                                    alt={recipe.recipe_name} 
                                    style="width: 100%; height: 200px; object-fit: cover; border-radius: 6px; margin-top: 0.5rem;" 
                                />
                            {/if}
                            <div style="display: flex; gap: 0.5rem; margin-top: 1rem;">
								<button 
									onclick={() => editingId = recipe.id} 
									style="background: #ff9800; color: white; border: none; padding: 0.3rem 0.6rem; border-radius: 4px; cursor: pointer; font-size: 0.8rem;"
								>Edit</button>

								<form method="POST" action="?/remove" use:enhance>
									<input type="hidden" name="id" value={recipe.id} />
									<button 
										type="submit" 
										style="background: #f44336; color: white; border: none; padding: 0.3rem 0.6rem; border-radius: 4px; cursor: pointer; font-size: 0.8rem;"
										onclick={() => !confirm('Are you sure?') && event.preventDefault()}
									>Delete</button>
								</form>
							</div>
                        {/if}
					</article>
				{/each}
			</div>
		{:else}
			<div style="text-align: center; padding: 3rem; color: #999; border: 2px dashed #eee;">
				<p>No recipes found.</p>
				<p style="font-size: 0.8rem;">Start by adding your first recipe above!</p>
			</div>
		{/if}
	</section>
</main>