<script setup>
  import { ref } from 'vue'
  import { useArticleStore } from '../stores/articles';

  const store = useArticleStore()

  const title = ref(null)
  const content = ref(null)

</script>

<template>
  <div>
    <h1>게시글 생성 페이지</h1>
    <form @submit.prevent="store.createArticle(title, content)">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model="title">
      <label for="content">내용 : </label>
      <input type="text" id="content" v-model="content">
      <input type="submit" value="create">
    </form>
  </div>
</template>

<style scoped>

</style>