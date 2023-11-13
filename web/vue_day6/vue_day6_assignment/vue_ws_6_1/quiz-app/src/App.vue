<script setup>
  import { RouterLink, RouterView } from 'vue-router'
  import MainPage from '@/components/MainPage.vue'
</script>

<template>
  <header>
    <MainPage />
    <nav>
      <RouterLink class="link" :to="{name: 'home'}">Home</RouterLink>
      |
    </nav>
  </header>

  <RouterView />
</template>

<style scoped>
  header {
    width: 60%;
    text-align: center;
    margin: auto;
    background-color: #F0F0F0;
    padding: 1rem;
  }

  nav {
    background-color: black;
    margin-top: 1rem;
    color: white;
    padding: .5rem 0;
    font-size: 13px;
  }

  .link {
    color: white;
    text-decoration: none;
  }
</style>