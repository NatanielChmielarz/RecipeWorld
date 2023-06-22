<script>
	import { onMount } from 'svelte';
	import Dish from './Dish.svelte';
  	import RecipeDisplay from './RecipeDisplay.svelte';
  import DishForm from './DishForm.svelte';
  
	let data = [];
  
	onMount(async () => {
	  try {
		const response = await fetch('http://127.0.0.1:8000/dish');
		data = await response.json();
	  } catch (error) {
		console.error('Błąd pobierania danych:', error);
	  }
	});
  
	function countRecipes(recipes) {
	  return recipes.length;
	}
  </script>
  
  <main>
	<DishForm/>
	{#if data.length > 0}
	  <h1>Dania</h1>
	  {#each data as item}
		<Dish id ={item.id} Name={item.name} Recipe_count={countRecipes(item.recipes)} Description={item.description} />
		<h4>Przepisy:</h4>
		{#each item.recipes as recipe}
		  
			<RecipeDisplay Author={recipe.author} Ingredients={recipe.ingredients } Instructions={recipe.instructions} />
			
		  
		{/each}
	  {/each}
	{:else}
	  <p>Trwa pobieranie danych...</p>
	{/if}
  </main>
  <style> main{padding: 60px 150px;
    background-color: #fff;
    border-radius: 45px;}
</style>