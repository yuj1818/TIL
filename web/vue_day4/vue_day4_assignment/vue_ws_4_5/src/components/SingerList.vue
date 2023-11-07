<template>
    <div class="singer-list">
        <h1>가수 목록</h1>
        <div class="singer-card-list">
            <SingerDetail v-for="singer in singers" :key="singer.name" />
        </div>
    </div>

</template>

<script setup>
    import SingerDetail from './singers/SingerDetail.vue';
    import { ref } from 'vue'

    const singers = ref([
        {name: 'adele'},
        {name: 'marron 5'},
        {name: 'Dua Lipa'}
    ])
</script>

<style scoped>
    .singer-list {
        text-align: center;
    }

    h1 {
        color: orangered;
    }

    .singer-card-list {
        text-align: center;
    }

    #card {
        display: inline-block;
        width: 40%;
        margin: 20px;
        border: 1px solid black;
        text-align: center;
    }
</style>