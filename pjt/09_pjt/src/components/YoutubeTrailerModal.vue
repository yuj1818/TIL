<script setup>
  import { ref, computed } from 'vue'
  import axios from 'axios'
  
  const props = defineProps({
    movie: Object
  })

  const searchList = ref([])

  axios({
    method: 'get',
    url: 'https://www.googleapis.com/youtube/v3/search',
    params: {
      key: import.meta.env.VITE_YOUTUBE_API_KEY,
      part: 'snippet',
      type: 'video',
      q: `${props.movie.title} 공식 예고편`
    }
  })
    .then(res => {
      searchList.value = res.data.items
      console.log(searchList.value)
    })

  const isNotEmpty = computed(() => {
    return searchList.value.length > 0
  })

  const getVideoUrl = function() {
    return `https://www.youtube.com/embed/${searchList.value[0].id.videoId}`
  }

</script>

<template>
  <div class="shadow">
    <div class="modal" @click.stop>
      <div class="text">
        <p class="title">{{ props.movie.title }} 공식 예고편</p>
      </div>
      <hr>
      <div class="frame">
        <iframe class="video" v-if="isNotEmpty" :src="getVideoUrl()"></iframe>
      </div>
    </div>
  </div>
</template>

<style scoped>
  .shadow {
    position: fixed;
    top: 0;
    right: 0;
    left: 0;
    bottom: 0;
    background-color: rgba(0, 0, 0, 0.7);
  }

  .modal {
    background-color: white;
    width: 60%;
    height: 50%;
    padding: 5px 0;
    margin: .5rem auto;
    border-radius: 5px;
  }

  hr {
    margin: 0;
  }

  .text {
    height: 20%;
    display: flex;
    align-items: center;
  }

  .title {
    font-size: small;
    font-weight: bold;
    text-align: start;
    margin: 0;
    margin-left: 1rem;
  }

  .video {
    width: 100%;
    height: 90%;
  }

  .frame {
    display: flex;
    align-items: center;
    width: 80%;
    height: 80%;
    margin: 0 auto;
  }
</style>
