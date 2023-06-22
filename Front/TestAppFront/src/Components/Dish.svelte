<script>
    export let id
    export let Name
    export let Description
    export let Recipe_count=0;
    function refreshPage() {
      location.reload(); // Odśwież stronę
    }
    async function HandleDelete() {
    try {
      const res = await fetch(`http://127.0.0.1:8000/dish/${id}`, {
        method: 'DELETE'
      });

      if (res.ok) {
        console.log('Dish deleted successfully!');
        refreshPage();
      } else {
        console.error('Failed to delete dish');
        // Tutaj możesz umieścić kod obsługujący błąd usuwania rekordu
      }
    } catch (error) {
      console.error('Error occurred while deleting dish:', error);
      // Tutaj możesz umieścić kod obsługujący błąd żądania
    }
  }
</script>


<div class="card">
  <div class="content">
    <div class="icon">
      <svg id="Layer_1" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 122.88 122.88">
        <title>meal-food</title>
        <path d="M61.44,0A61.46,61.46,0,1,1,18,18,61.21,61.21,0,0,1,61.44,0ZM52.55,58.42c2.92-2,4.39-4.61,4.14-10.58V32.49c0-2.14-3.92-2.4-4.11,0l-.15,12.45a1.75,1.75,0,1,1-3.5,0l.15-12.88c0-2.3-3.77-2.53-3.81,0,0,3.58-.15,9.31-.15,12.88a1.52,1.52,0,1,1-3,0l.15-12.79A2.09,2.09,0,0,0,39,30.61c-1.38.88-1.1,2.65-1.16,4.15l-.48,14.69c.07,4.27,1.19,7.74,4.54,9.22a8.37,8.37,0,0,0,2,.52L42.77,89.25a3.76,3.76,0,0,0,3.71,3.86h.46a4.24,4.24,0,0,0,4.17-4.34l-1-29.59a6.61,6.61,0,0,0,2.45-.76Zm18,29.75-.05-26.41c-11.29-6.52-7.69-31.64,3.6-31.5,13.72.16,15.35,28.31,3.55,31.4l.87,26.64c.17,6.13-8,6.7-8-.13ZM99.29,23.59A53.52,53.52,0,1,0,115,61.44,53.36,53.36,0,0,0,99.29,23.59Z"/>
      </svg>
    </div>
    <div class="text">
      <h1>{Name}</h1>
      <p>{Description}</p>
      <span> Ilosc przepisow : {Recipe_count}</span>
    </div>
    <div class="buttons">
      <button><i class="fas fa-pen"></i></button>
      <button><i class="fas fa-plus"></i></button>
      <button on:click={HandleDelete}><i class="fas fa-trash"></i></button>
    </div>
  </div>
</div>

<style>
  i{width: 24px;}
  .card {
    margin-top: 20px;
    align-items: center;
    border: 2px solid #ccc;
    border-radius: 8px;
    padding: 20px;
  }

  .content {
    display: flex;
    align-items: center;
  }

  .icon {
    margin-right: 16px;
  }

  #Layer_1 {
    width: 64px;
    fill: #8899E7;
  }

  .text {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
  }

  h1 {
    font-weight: bold;
    font-size: 24px;
    margin-bottom: 8px;
    color: #333;
  }

  p {
    font-size: 16px;
    color: #666;
    margin-bottom: 16px;
  }

  span {
    text-align: center;
    font-size: 16px;
    color: #666;
  }

  .buttons {
    margin-left: auto;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
  }

  button {
    background-color: #007bff;
    color: #fff;
    border: none;
    padding: 8px 16px;
    font-size: 16px;
    border-radius: 4px;
    cursor: pointer;
    margin-bottom: 8px;
  }

  button:hover {
    background-color: #0056b3;
  }
</style>