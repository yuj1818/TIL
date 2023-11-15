<script setup>
  defineProps({
    product: Object
  })
</script>

<template>
  <div class="card">
    <h3>{{ product.name }}</h3>
    <img class="item-img" :src="product.imagePath" alt="">
    <p>\ {{ product.price }}</p>
    <img v-if="product.isFavorite" src="../assets/like.png" alt="like">
    <img v-else src="../assets/unlike.png" alt="unlike">
  </div>
</template>

<style scoped>
  .card {
    width: 28%;
    border: 1px solid gainsboro;
    padding: 1rem;
    text-align: center;
  }

  .item-img {
    width: 100%;
  }
</style>
