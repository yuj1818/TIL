<script setup>
  const props = defineProps({
    video: Object
  })

  const getVideoUrl = function() {
    return `https://www.youtube.com/embed/${props.video.id.videoId}`
  }
</script>

<template>
  <div class="shadow">
    <div class="modal" @click.stop>
      <div class="text">
        <p class="title">{{ props.video.snippet.title }}</p>
      </div>
      <hr>
      <div class="frame">
        <iframe class="video" :src="getVideoUrl()"></iframe>
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
    width: 50%;
    height: 50%;
    margin: 1rem auto;
    border-radius: 5px;
    text-align: center;
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