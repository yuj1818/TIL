<script setup>
  import axios from 'axios'
  import { ref, computed } from 'vue'
  import MovieCard from '../components/MovieCard.vue'
  import { useRouter } from 'vue-router'

  const router = useRouter()

  const ratedMovies = ref([])

  axios({
    method: 'get',
    url: 'https://api.themoviedb.org/3/movie/top_rated',
    params: {
      api_key: import.meta.env.VITE_TMDB_API_KEY,
      language: 'ko-KR',
    }
  })
    .then(res => {
      //console.log(res.data)
      ratedMovies.value = res.data.results
    })

  const isValid = computed(() => {
    return ratedMovies.value.length > 0
  })

  const goDetail = function(id) {
    router.push({name: 'detail', params: {movieId: id}})
  }
</script>

<template>
  <div class="container">
    <MovieCard 
      v-if="isValid"
      v-for="movie in ratedMovies" 
      :key="movie.id" 
      :movie="movie" 
      @click="goDetail(movie.id)"
    />
  </div>
</template>

<style scoped>
  .container {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
  }

</style>
