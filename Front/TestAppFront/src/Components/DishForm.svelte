<style>
   
    .container {
      max-width: 400px;
      margin: 0 auto;
      background-color: #fff;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
  
    .title {
      font-size: 24px;
      font-weight: bold;
      margin-bottom: 20px;
      text-align: center;
      color: #333;
    }
  
    .error-message {
      color: red;
      margin-bottom: 10px;
      text-align: center;
    }
  
    .input-field {
      margin-bottom: 10px;
      padding: 8px;
      border: 1px solid #ccc;
      border-radius: 4px;
      font-size: 14px;
      width: 100%;
      box-sizing: border-box;
    }
  
    .submit-button {
      display: block;
      width: 100%;
      padding: 8px 16px;
      background-color: #007bff;
      color: #fff;
      border: none;
      border-radius: 4px;
      font-size: 16px;
      cursor: pointer;
    }
  
    .submit-button:hover {
      background-color: #0056b3;
    }
  </style>
  
  <script>
    import { createEventDispatcher } from 'svelte';
  
    let name = '';
    let description = '';
    let errorMessage = '';
  
    const dispatch = createEventDispatcher();
  
    async function doPost() {
      if (!validateInputs()) {
        return;
      }
  
      try {
        const res = await fetch('http://127.0.0.1:8000/dish/', {
          method: 'POST',
          body: JSON.stringify({
            name,
            description
          })
        });
  
        const json = await res.json();
        const result = JSON.stringify(json);
  
        if (res.ok) {
          // Handle successful response, if needed
          console.log('Dish added successfully!');
          refreshPage(); // Odśwież stronę
        } else {
          // Handle error response, if needed
          console.error('Failed to add dish');
        }
      } catch (error) {
        console.error('Error occurred while adding dish:', error);
      }
  
      dispatch('submit');
    }
  
    function validateInputs() {
      errorMessage = '';
  
      if (name.length < 5 || description.length < 10) {
        errorMessage = 'Name must be at least 5 characters long and description must be at least 10 characters long.';
        return false;
      }
  
      return true;
    }
  
    function refreshPage() {
      location.reload(); // Odśwież stronę
    }
  </script>
  
  <div class="container">
    <h1 class="title">Brakuje Twojego ulubionego dania? Dodaj je już teraz!</h1>
  
    {#if errorMessage}
      <p class="error-message">{errorMessage}</p>
    {/if}
  
    <input bind:value={name} placeholder="Name" class="input-field" />
    <input bind:value={description} placeholder="Description" class="input-field" />
  
    <button type="button" on:click={doPost} class="submit-button">
      Add Dish
    </button>
  </div>
  