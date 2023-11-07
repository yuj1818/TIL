<template>
    <div class="singer-list">
        <h1>가수 목록</h1>
        <div class="singer-card-list">
            <SingerDetail />
            <SingerDetail />
        </div>
    </div>

</template>

<script setup>
    import SingerDetail from './singers/SingerDetail.vue';
</script>

<style scoped>
    .singer-list {
        text-align: center;
    }

    h1 {
        color: orangered;
    }

    .singer-card-list {
        display: flex;
        justify-content: center;
        width: 100%;
    }

    #card {
        display: inline-block;
        width: 40%;
        margin: 20px;
        border: 1px solid black;
        text-align: center;
    }
</style>