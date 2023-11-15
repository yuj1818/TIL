<script setup>
  import { useProductsStore } from '../stores/products';

  const store = useProductsStore()

  defineProps({
    product: Object
  })
</script>

<template>
  <div class="card">
    <h3>{{ product.name }}</h3>
    <img class="item-img" :src="product.imagePath" alt="">
    <p>\ {{ product.price }}</p>
    <button class="favorite-btn" v-if="product.isFavorite" @click="store.toggleFavorite(product.name)">
      <img src="../assets/like.png" alt="like">
    </button>
    <button class="favorite-btn" v-else @click="store.toggleFavorite(product.name)">
      <img src="../assets/unlike.png" alt="unlike">
    </button> 
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

  .favorite-btn {
    border: none;
    background-color: white;
  }
</style>
