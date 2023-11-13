<template>
  <div class="child">
    <h3>자식 페이지</h3>
    <p>{{ name }}</p>
  </div>
</template>

<script setup>
  defineProps({
    name: String
  })
</script>

<style scoped>
  .child {
    border: 1px solid lightgrey;
    background-color: white;
    margin: .5rem;
  }
</style>