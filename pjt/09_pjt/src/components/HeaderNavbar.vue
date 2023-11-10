<script setup>
  import { useRoute, RouterLink, useRouter } from 'vue-router'
  import { ref, watch } from 'vue'

  const route = useRoute()
  const router = useRouter()

  const path = ref()

  const goHome = function() {
    router.push({name: 'home'})
  }

  watch(route, (to, from) => {
    // console.log(to.path)
    // console.log(from.path)
    path.value = to.path
  })
  
</script>

<template>
  <div class="navbar">
    <img class="logo" src="../assets/ssafy_logo.png" alt="" @click="goHome">
    <div class="nav-item">
      <RouterLink :class="{current: path === '/movies'}" :to="{name: 'movies'}">영화조회</RouterLink>
      <RouterLink :class="{current: path === '/review-search'}" :to="{name: 'search'}">리뷰검색</RouterLink>
      <RouterLink :class="{current: path === '/recommended'}" :to="{name: 'recommend'}">영화추천</RouterLink>
    </div>
  </div>
</template>

<style scoped>
  .navbar {
    position: fixed;
    top: 0;
    right: 0;
    left: 0;
    height: 50px;
    background-color: lightgrey;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 .5rem
  }

  .logo {
    height: 40px;
  }

  .logo:hover {
    cursor: pointer;
  }

  a {
    color: dimgray;
    font-weight: bold;
    text-decoration: none;
    font-size: 14px;
    margin-left: .5rem;
  }

  .current {
    color: green;
  }
</style>
