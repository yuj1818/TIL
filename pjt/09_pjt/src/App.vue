<script setup>
  import { RouterView } from 'vue-router'
  import HeaderNavbar from './components/HeaderNavbar.vue';
</script>

<template>
  <HeaderNavbar />
  <RouterView class="container" />
</template>

<style scoped>
  .container {
    width: 90%;
    margin: 80px auto;
  }
</style>
