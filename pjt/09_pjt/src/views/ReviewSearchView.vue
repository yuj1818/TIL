<script setup>
  import axios from 'axios'
  import { ref, computed } from 'vue'
  import YoutubeCard from '../components/YoutubeCard.vue';
  import YoutubeReviewModal from '../components/YoutubeReviewModal.vue';

  const searchResults = ref([])

  const keyword = ref('')

  const onSearch = function() {
    axios({
      method: 'get',
      url: 'https://www.googleapis.com/youtube/v3/search',
      params: {
        key: import.meta.env.VITE_YOUTUBE_API_KEY,
        part: 'snippet',
        type: 'video',
        q: `영화 ${keyword.value} 리뷰`
      }
    })
      .then(res => {
        console.log(res.data.items)
        searchResults.value = res.data.items
      })
  }

  const isNotEmpty = computed(() => {
    return searchResults.value.length > 0
  })

  const modalId = ref()

  const showVideo = function(id) {
    modalId.value = id
  }

  const closeVideo = function() {
    modalId.value = null
  }

</script>

<template>
  <div class="container">
    <form class="search-form" @submit.prevent="onSearch">
      <input v-model="keyword" class="keyword" type="text" placeholder="영화 제목을 검색해보세요">
      <button class="search-btn" type="submit">검색</button>
    </form>
    <div class="search-result">
      <div v-if="isNotEmpty" v-for="video in searchResults" :key="video.id.videoId">
        <YoutubeCard 
          :video="video" 
          @click="showVideo(video.id.videoId)"
        />
        <YoutubeReviewModal v-if="modalId === video.id.videoId" :video="video" @click="closeVideo" />
      </div>
    </div>
  </div>
</template>

<style scoped>
  .search-form {
    display: flex;
    gap: .5rem;
    justify-content: center;
  }

  .keyword {
    width: 60%;
    border: 1px solid grey;
    border-radius: 3px;
    padding: .3rem;
    font-size: 15px;
  }

  .search-btn {
    background-color: dodgerblue;
    color: white;
    border-radius: 3px;
    border: none;
    padding: .3rem 1rem;
    font-size: 15px;
  }

  .search-result {
    margin-top: 1rem;
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }
</style>
