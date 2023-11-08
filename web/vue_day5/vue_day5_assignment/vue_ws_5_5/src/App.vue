<template>
  <div>
      <h1>명함 관리 페이지</h1>
      <p>명함을 관리하는 페이지입니다. 여기에 명함 목록이 표시됩니다.</p>
      <CreateCardForm @create-card-event="updateCard"/>
      <article>
          <BusinessCard :new-card="newCard" />
      </article>
  </div>
</template>

<script setup>
  import BusinessCard from './components/BusinessCard.vue';
  import CreateCardForm from './components/CreateCardForm.vue';
  import { ref } from 'vue'

  const newCard = ref(null)
  
  const updateCard = function(cardInfo) {
    newCard.value = cardInfo
  }
</script>

<style scoped>
  h1 {
      background-color: dodgerblue;
      color: white;
      width: 30%;
      text-align: center;
      padding: 3rem 1rem;
  }

  div {
      display: flex;
      flex-direction: column;
      align-items: center;
  }

  article {
      width: 100%;
  }
</style>