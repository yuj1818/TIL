<template>
  <nav>
    <RouterLink :to="{name: 'home'}">Home</RouterLink>
    <RouterLink :to="{name: 'products'}">Products</RouterLink>
    <RouterLink :to="{name: 'favorite'}">Favorite</RouterLink>
  </nav>
</template>

<script setup>
  import { RouterLink } from 'vue-router'
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
</style>