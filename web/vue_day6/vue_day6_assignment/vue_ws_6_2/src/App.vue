<script setup>
  import { RouterLink, RouterView } from 'vue-router';
  import MainPage from '@/components/MainPage.vue';
</script>

<template>
  <div class="quiz-app">
    <MainPage />
    <nav class="app-nav">
      <RouterLink :to="{name: 'home'}" class="nav-link">Home</RouterLink> | 
      <RouterLink :to="{name: 'quiz'}" class="nav-link">Quiz</RouterLink> |
    </nav>
  </div>
  
  <RouterView />
</template>

<style scoped>
  .quiz-app {
    width: 60%;
    text-align: center;
    margin: auto;
    background-color: #F0F0F0;
    padding: 1rem;
    margin-bottom: 4rem;
  }

  .app-nav {
    background-color: black;
    margin-top: 1rem;
    color: white;
    padding: .5rem 0;
    font-size: 13px;
  }

  .nav-link {
    color: white;
    text-decoration: none;
  }
</style>
