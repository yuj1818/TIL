<template>
    <div class="albums">
        <h4>앨범 제목</h4>
        <p class="orangered song" v-for="songNum in [1, 2, 3]" :key="songNum">노래 목록 {{ songNum }}</p>
    </div>
</template>

<style scoped>
    .orangered {
        color: orangered;
    }

    .song {
        margin: 5px 0px;
    }

    .albums {
        text-align: center;
        border: 1px solid lightgrey;
        border-radius: 10px;
        padding: 1rem;
        padding-top: 0;
        background-color: gainsboro;
    }
</style>