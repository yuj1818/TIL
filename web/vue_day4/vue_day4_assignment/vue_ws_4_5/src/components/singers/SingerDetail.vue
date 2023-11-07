<template>
    <div id="card">
        <h1>가수 이름</h1>
        <img src="../../assets/singer.jpg" alt="singer.jpg" class="singer_img">
        <p>가수 소개글</p>
        <div class="album-list">
            <SingerAlbum />
            <SingerAlbum />
        </div>
    </div>
</template>

<script setup>
    import SingerAlbum from './SingerAlbum.vue';
</script>

<style scoped>
    .singer_img {
        width: 200px;
        border-radius: 50%;
    }

    .album-list {
        display: flex;
        gap: 1rem;
        margin-bottom: 1rem;
        justify-content: center;
    }
</style>

<!-- <style>
    h1 {
        color: green;
    }
</style> -->