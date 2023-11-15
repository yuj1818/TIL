<template>
  <div class="article-list">
    <button><RouterLink class="link" :to="{name: 'create'}">게시글 생성</RouterLink></button>
    <div 
      class="article"
      v-for="(article, idx) in store.articles"
      :key="article.title"
    >
      <h3>{{ idx + 1 }}번 게시글</h3>
      <p>제목 : {{ article.title }}</p>
      <p>내용 : {{ article.content }}</p>
      <hr>
    </div>
  </div>
</template>

<script setup>
  import { onMounted } from 'vue'
  import { useArticleStore } from '@/stores/articles'
  import { RouterLink } from 'vue-router'
  const store = useArticleStore()

  onMounted(() => {
    store.getArticles()
  })
</script>

<style scoped>
  .link {
    text-decoration: none;
  }

  .link:visited {
    color: black;
  }
</style>