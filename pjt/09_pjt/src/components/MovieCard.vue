<script setup>
  defineProps({
    movie: Object
  })

  const image = function(path) {
    return `https://image.tmdb.org/t/p/original/${path}`
  }
</script>

<template>
  <div class="card">
    <img class="card-img" :src=image(movie.poster_path) alt="">
    <div class="card-text">
      <p class="title">{{ movie.title }}</p>
      <p class="description">{{ movie.overview }}</p>
    </div>
  </div>
</template>

<style scoped>
  .card-img {
    width: 100%;
  }

  .card {
    width: 30%;
    border: 1px solid gainsboro;
  }

  .card-text {
    margin: 0 1rem;
  }

  .title {
    font-weight: bold;
  }

  .description {
    font-size: small;
  }
</style>
