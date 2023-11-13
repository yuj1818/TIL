<script setup>
  import { useCounterStore } from '@/stores/counter'

  const store = useCounterStore()

  console.log(store.count)
  const newNumber = store.count + 1

  // getters 참조
  console.log(store.doubleCount)

  // actions 호출
  store.increment()
</script>

<template>
  <div>
    <p>state : {{ store.count }}</p>
  </div>
  
  <div>
    <p>getters : {{ store.doubleCount }}</p>
  </div>

  <div>
    <button @click="store.increment()">+++</button>
  </div>
</template>

<style scoped>
</style>
