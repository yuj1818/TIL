<template>
    <div class="singer-detail">
        <h1>가수 이름</h1>
        <img src="../../assets/singer.jpg" alt="singer.jpg" class="singer_img">
        <p>가수 소개글</p>
    </div>
</template>

<style scoped>
    .singer-detail {
        display: flex;
        flex-direction: column;
        align-items: center;
        border: 1px solid black;
        width: 100%;
    }

    .singer_img {
        width: 200px;
        border-radius: 50%;
    }
</style>