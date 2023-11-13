<script setup>
  import { ref } from 'vue'

  const question = ref('')
  const answer = ref('')

  const emit = defineEmits(['createQuiz'])
  const createQuiz = function () {
    emit('createQuiz', {question: question.value, answer: answer.value})
    question.value = ''
    answer.value = ''
  }
</script>

<template>
    <div class="quiz-create-container">
      <h3>퀴즈 생성</h3>
      <form class="quiz-create-form" @submit.prevent="createQuiz">
        <div class="input">
          <label for="question">문제</label>
          <textarea id="question" cols="30" rows="5" v-model="question"></textarea>
        </div>
        <div class="input">
          <label for="answer">답안</label>
          <input type="text" id="answer" v-model="answer">
        </div>
        <button class="create-btn" type="submit">퀴즈 생성</button>
      </form>
    </div>
</template>

<style scoped>
  .quiz-create-container {
    border-radius: 10px;
    background-color: #F0F0F0;
    padding: 1rem;
    width: 60%;
  }

  .quiz-create-form {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .input {
    display: flex;
    flex-direction: column;
    gap: .5rem;
  }

  #question {
    border: 1px solid lightgrey;
    border-radius: 5px;
    resize: none;
  }

  #answer {
    border: 1px solid lightgrey;
    border-radius: 5px;
    padding: .5rem;
  }

  label {
    font-size: 13px;
  }

  .create-btn {
    background-color: dodgerblue;
    border-radius: 5px;
    border: none;
    color: white;
    padding: .5rem;
  }
</style>