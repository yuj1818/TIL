<script setup>
  import { useProductsStore } from '../stores/products'
  import ProductDetail from '../components/ProductDetail.vue'

  const store = useProductsStore()
</script>

<template>
  <div>
    <h1>장바구니 페이지</h1>
    <div class="favorite-list">
      <ProductDetail 
        v-for="product in store.favoriteProducts"
        :key="product.name"
        :product="product"
      />
    </div>
  </div>
</template>

<style scoped>
  .favorite-list {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    row-gap: 1rem;
  }
</style>
