<script setup>
  defineProps({
    video: Object
  })
</script>

<template>
  <div class="card">
    <img :src="video.snippet.thumbnails.default.url" alt="">
    <div class="card-content">
      <h3>{{ video.snippet.title }}</h3>
      <p class="description">{{ video.snippet.description }}</p>
    </div>
  </div>
</template>

<style scoped>
  .card {
    display: flex;
    border: 1px solid gainsboro;
    border-radius: 5px;
    padding: .5rem;
    gap: .5rem;
  }

  .description {
    font-size: small;
  }
</style>
