<script setup>
  import { RouterLink, RouterView } from 'vue-router'
  import MainView from './views/MainView.vue';
</script>

<template>
  <div>
    <nav>
      <RouterLink :to="{name: 'main'}">main</RouterLink>
    </nav>
    <h1>pinia + router 연습하기</h1>
    <RouterView />
  </div>
</template>

<style scoped>
</style>
