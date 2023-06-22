<script>
  export let Author;
  export let Ingredients;
  export let Instructions;
  let IconChanger = "fa-arrow-down";
  let isContentVisible = false;
  
  function change() {
    isContentVisible = isContentVisible ? false : true;
    IconChanger = IconChanger == "fa-arrow-down" ? "fa-arrow-up" : "fa-arrow-down";
  }
</script>

<main>
  <div class="Recipes">
    <i class="fas fa-user"></i>
    <h4>Autor: {Author}</h4>
    <div class="buttons">
        <button><i class="fas fa-pen"></i></button>
        <button on:click={change}><i class="fas {IconChanger}"></i></button>
        <button><i class="fas fa-trash"></i></button>
      </div>
</div>

  {#if isContentVisible}
    <div class="Content">
      <p><strong>Składniki:</strong> {Ingredients}</p>
      <p><strong>Instrukcje:</strong> {Instructions}</p>
    </div>
  {/if}
</main>
<style>
    .Recipes {
    display: flex;
    justify-content: flex-start;
    align-items: center;
    gap: 10px;
    padding: 10px 20px;
    width:fit-content;
    border-radius: 25px;
  }
  .Recipes:hover{background-color: #b4c5d6;}
  .Content{padding: 20px;}
  button {
    background-color: #007bff;
    color: #fff;
    border: none;
    padding: 4px 8px;
    font-size: 12px;
    border-radius: 2px;
    cursor: pointer;
    margin-bottom: 4px;
  }

  button:hover {
    background-color: #0056b3;
  }
</style>
