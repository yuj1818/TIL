import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useProductsStore = defineStore('products', () => {
  const productList = ref([
    {
      name: '상품 1',
      imagePath: 'src/assets/product1.png',
      price: 10000,
      isFavorite: false
    },
    {
      name: '상품 2',
      imagePath: 'src/assets/product2.png',
      price: 20000,
      isFavorite: false
    },
    {
      name: '상품 3',
      imagePath: 'src/assets/product3.png',
      price: 30000,
      isFavorite: false
    },
    {
      name: '상품 4',
      imagePath: 'src/assets/product4.png',
      price: 40000,
      isFavorite: false
    }
  ])

  const toggleFavorite = function (name) {
    const idx = productList.value.findIndex(product => product.name === name)
    productList.value[idx].isFavorite = !productList.value[idx].isFavorite
  }

  const countFavorite = computed(() => {
    return productList.value.filter(product => product.isFavorite === true).length
  })

  return { productList, toggleFavorite, countFavorite }
})