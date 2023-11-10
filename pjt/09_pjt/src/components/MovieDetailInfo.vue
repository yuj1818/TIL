<script setup>
  import YoutubeTrailerModal from './YoutubeTrailerModal.vue';
  import { ref } from 'vue'

  defineProps({
    info: Object
  })

  const image = function(path) {
    return `https://image.tmdb.org/t/p/original/${path}`
  }

  const modalShow = ref(false)

  const showTrailer = function() {
    modalShow.value = true
  }
 
  const closeTrailer = function() {
    modalShow.value = false
  }
</script>

<template>
  <div class="info">
    <img class="movie-img" :src="image(info.poster_path)" alt="">
    <h4>{{ info.title }}</h4>
    <p class="sm-font"><b>개봉일: </b>{{ info.release_date  }}</p>
    <p class="sm-font"><b>러닝타임: </b>{{ info.runtime }} 분</p>
    <p class="sm-font"><b>TMDB 평점: </b>{{ info.vote_average }}</p>
    <h4>장르</h4>
    <div class="genre">
      <p class="sm-font" v-for="genre in info.genres" :key="genre.id">{{ genre.name }}</p>
    </div>
    <h4>줄거리</h4>
    <p class="sm-font">{{ info.overview }}</p>
    <h4>공식 예고편</h4>
    <img src="../assets/youtube.svg" alt="" @click="showTrailer">
    <YoutubeTrailerModal v-if="modalShow" :movie="info" @click="closeTrailer" />
  </div>
</template>

<style scoped>
  .info {
    text-align: center;
  }
  .movie-img {
    width: 20%;
  }

  .sm-font {
    font-size: small;
  }

  .genre {
    display: flex;
    gap: 1rem;
    justify-content: center;
  }
</style>
