<template>
  <div>
      <h2>보유 명함 목록</h2>
      <p v-if="businessCards.length">현재 보유중인 명함 수 : {{  businessCards.length }}</p>
      <p v-else>명함이 없습니다. 새로운 명함을 추가해 주세요.</p>
      <div class="card-list">
          <businessCardDetail 
              v-for="card in businessCards" 
              :key="card" :info="card" 
              @delete-card-event="deleteCard" 
          />
      </div>
  </div>
</template>

<script setup>
  import businessCardDetail from './businessCardDetail.vue';
  
  import { ref, watch } from 'vue'

  const props = defineProps({
    newCard: Object
  })
  
  const businessCards = ref([
      {name: '일론 머스크', title: '테슬라 테크노킹'},
      {name: '래리 엘리슨', title: '오라클 창업주'},
      {name: '빌 게이츠', title: '마이크로소프트 공동창업주'},
      {name: '래리 페이지', title: '구글 공동창업주'},
      {name: '세르게이 브린', title: '구글 공동창업주'}
  ])

  const deleteCard = function(info) {
      const filteredCards = businessCards.value.filter(card => card != info)
      businessCards.value = filteredCards
  }

  watch(() => props.newCard, (card) => businessCards.value.push(card))
</script>

<style scoped>
  .card-list {
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
      gap: 1rem;
      width: 100%;
  }
</style>