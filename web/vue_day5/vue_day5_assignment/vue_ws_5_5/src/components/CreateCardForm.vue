<template>
  <div>
    <form @submit.prevent="createCardFunc">
      <label for="name">이름</label>
      <input id="name" type="text" v-model="name">
      <label for="title">직함</label>
      <input id="title" type="text" v-model="title">
      <button type="submit">명함 추가</button>
    </form>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const name = ref('')
  const title = ref('')

  const emit = defineEmits(['createCardEvent'])

  const createCardFunc = function () {
    const cardInfo = {name: name.value, title: title.value}
    emit('createCardEvent', cardInfo)
    name.value = ''
    title.value = ''
  }
</script>

<style scoped>
  form > * {
    margin-right: .5rem;
  }

  form {
    display: flex;
    align-items: center;
  }

  input {
    padding: 8px 0;
    border: 1px solid dodgerblue;
    border-radius: 5px;
  }

  label {
    font-weight: bold;
  }

  button {
    border: 1px solid dodgerblue;
    border-radius: 5px;
    background-color: white;
    color: dodgerblue;
    padding: 8px;
  }
</style>