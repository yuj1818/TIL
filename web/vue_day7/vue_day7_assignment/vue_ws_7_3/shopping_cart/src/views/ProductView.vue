<script setup>
  import { useProductsStore } from '../stores/products'
  import ProductDetail from '../components/ProductDetail.vue';

  const store = useProductsStore()
</script>

<template>
  <div>
    <h1>상품 목록 페이지</h1>
    <div class="item-list">
      <ProductDetail
        v-for="product in store.productList"
        :key="product.name"
        :product="product"
      />
    </div>
  </div>
</template>

<style scoped>
  .item-list {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    row-gap: 1rem;
  }
</style>
