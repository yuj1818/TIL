<template>
  <nav>
    <RouterLink :to="{name: 'home'}">Home</RouterLink>
    <RouterLink :to="{name: 'products'}">Products</RouterLink>
    <div class="favorite">
      <RouterLink :to="{name: 'favorite'}">Favorite</RouterLink>
      <div v-if="store.countFavorite" class="cnt-favorite">{{ store.countFavorite }}</div>
    </div>
  </nav>
</template>

<script setup>
  import { RouterLink } from 'vue-router'
  import { useProductsStore } from '../stores/products';

  const store = useProductsStore()
</script>

<style scoped>
  nav {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 50px;
    background-color: dimgray;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 2rem;
  }

  a {
    text-decoration: none;
    color: white;
    font-size: large;
  }

  .favorite {
    display: flex;
    gap: .5rem;
  }

  .cnt-favorite {
    align-self: flex-end;
    background-color: red;
    border-radius: 50%;
    color: white;
    width: 20px;
    height: 20px;
    text-align: center;
    font-size: small;
  }
</style>