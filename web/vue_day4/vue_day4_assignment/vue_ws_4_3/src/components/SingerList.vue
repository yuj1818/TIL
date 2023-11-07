<template>
    <div class="singer-list">
        <h1>가수 목록</h1>
        <SingerDetail />
    </div>

</template>

<script setup>
    import SingerDetail from './singers/SingerDetail.vue';
</script>

<style scoped>
    .singer-list {
        text-align: center;
    }
</style>