<script setup>
  import { ref, computed } from 'vue'
  import { useRoute } from 'vue-router'
  import axios from 'axios'
  import MovieDetailInfo from '../components/MovieDetailInfo.vue';

  const route = useRoute()
  
  const id = ref(route.params.movieId)

  const movieInfo = ref(null)

  axios({
    method: 'get',
    url: `https://api.themoviedb.org/3/movie/${id.value}`,
    params: {
      language: 'ko-KR',
      api_key: import.meta.env.VITE_TMDB_API_KEY
    }
  })
    .then(res => {
      console.log(res.data)
      movieInfo.value = res.data
    })

  const isNotEmpty = computed(() => {
    return movieInfo.value !== null
  })
</script>

<template>
  <div>
    <MovieDetailInfo v-if="isNotEmpty" :info="movieInfo" />
  </div>
</template>

<style scoped>

</style>
