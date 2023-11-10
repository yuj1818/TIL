<script setup>
  import { ref, computed } from 'vue'
  import axios from 'axios'
  import _ from 'lodash'
  
  const recommendedGenres = ref([])
  const weather = ref()
  const recommendedMovies = ref([])
  const genres = ref([])

  const recommendedMovie = ref()

  axios({
    method: 'get',
    url: 'https://api.openweathermap.org/data/2.5/weather',
    params: {
      q: 'Seoul,KR',
      appid: import.meta.env.VITE_WEATHER_API_KEY
    }
  })
    .then(res => {
      console.log(res.data)
      weather.value = res.data.weather[0].main

      if (weather.value == 'Thunderstrom') {
        recommendedGenres.value = ['공포', '범죄', '스릴러', '미스터리']
      } else if (weather.value == 'Drizzle') {
        recommendedGenres.value = ['드라마', '애니메이션', ]
      } else if (weather.value == 'Rain') {
        recommendedGenres.value = ['로맨스', '음악', '애니메이션']
      } else if (weather.value == 'Snow') {
        recommendedGenres.value = ['판타지', '가족', 'SF']
      } else if (weather.value == 'Clear') {
        recommendedGenres.value = ['모험', '액션', '코미디']
      } else if (weather.value == 'Clouds') {
        recommendedGenres.value = ['TV 영화', '전쟁']
      } else {
        recommendedGenres.value = ['역사', '서부', '다큐멘터리']
      }

      axios({
        method: 'get',
        url: 'https://api.themoviedb.org/3/genre/movie/list',
        params: {
          language: 'ko-KR',
          api_key: import.meta.env.VITE_TMDB_API_KEY
        }
      })
        .then(res => {
          genres.value = res.data.genres

          const transferGenres = []

          recommendedGenres.value.forEach(target => {
            transferGenres.push(genres.value.find(genre => genre.name === target).id)
          })

          console.log(transferGenres)

          axios({
            method: 'get',
            url: 'https://api.themoviedb.org/3/discover/movie',
            params: {
              api_key: import.meta.env.VITE_TMDB_API_KEY,
              language: 'ko-KR',
              with_genres: transferGenres.join('|')
            }
          })
            .then(res => {
              console.log(res.data.results)
              recommendedMovies.value = res.data.results
              recommendedMovie.value = _.sample(recommendedMovies.value)
              console.log(recommendedMovie.value)
            })
        })
    })

  const image = function(path) {
    return `https://image.tmdb.org/t/p/original/${path}`
  }

  const isNotEmpty = computed(() => {
    return recommendedMovies.value.length > 0
  })
  
</script>

<template>
  <div class="container">
    <h2>날씨 기반 추천 영화</h2>
    <p>현재 날씨: {{ weather }}</p>
    <img v-if="isNotEmpty" class="movie-img" :src="image(recommendedMovie.poster_path)" alt="">
  </div>
</template>

<style scoped>
  .container {
    text-align: center;
  }
  .movie-img {
    width: 40%
  }
</style>
