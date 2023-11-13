<script setup>
  import { useRoute } from 'vue-router';
  import { ref } from 'vue'
  const route = useRoute()

  const pk = ref(route.params.pk)
  const answer = ref(route.params.answer)
  const userAnswer = ref(route.query.userAnswer)
  const isRight = ref(answer.value === userAnswer.value)
  const isWrong = ref(answer.value != userAnswer.value)
</script>

<template>
    <div class="answer-container">
      <p class="sm num">{{ pk }}번 문제</p>
      <h3>정답 확인</h3>
      <div class="result">
        <p v-if="isRight" class="right"><b>정답입니다!</b></p>
        <p v-if="isWrong" class="wrong"><b>오답입니다.</b></p>
        <p class="sm" :class="{right:isRight, wrong:isWrong}">나의 제출 답안: {{ userAnswer }}</p>
        <p class="sm">정답: {{ answer }}</p>
      </div>
    </div>
</template>

<style scoped>
  .right {
    color: green;
  }

  .wrong {
    color: red;
  }

  .sm {
    font-size: 13px;
  }

  .num {
    margin: 0;
  }

  h3 {
    margin: 0;
  }

  .result {
    border: 1px solid lightgrey;
    background-color: white;
    border-radius: 10px;
    text-align: start;
    margin: .5rem;
    padding: 1rem
  }

  .answer-container {
    border: 1px solid lightgrey;
    border-radius: 10px;
    background-color: #F0F0F0;
    text-align: center;
  }
</style>