<template>
  <div class="quiz-container">
    <h4>{{ props.quiz.pk }}번 문제. {{ props.quiz.question }}</h4>
    <p>정답 입력</p>
    <input type="text" :id="props.quiz.pk">
  </div>
</template>

<script setup>
  const props = defineProps({
    quiz: Object
  })
</script>

<style scoped>
  .quiz-container {
    border: 1px solid lightgrey;
    border-radius: 10px;
    background-color: #F0F0F0;
    padding: 1rem;
    display: flex;
    flex-direction: column;
    margin: 1rem 0;
    width: 100%;
  }

  h4 {
    margin: 0;
  }

  p {
    font-size: 13px;
  }

  input {
    padding: .5rem;
    border: 1px solid lightgrey;
    border-radius: 5px;
  }
</style>