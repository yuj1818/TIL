<script setup>
  import { storeToRefs } from 'pinia';
  import { useBalanceStore } from '../stores/balance';
  import { useRoute } from 'vue-router'
  import { ref } from 'vue'

  const route = useRoute()
  const name = ref(route.params.name)
  const store = useBalanceStore()
  const { getUserInfo } = storeToRefs(store)
</script>

<template>
  <div>
    <h1>데이터 수정 페이지</h1>
    <p>이름: {{ name }}</p>
    <p>잔고: {{ getUserInfo(name).balance }}</p>
    <button @click="store.addBalance(name)">+</button>
  </div>
</template>
