<template>
    <div>
        <h3>자식 페이지입니다.</h3>
        <p>이름 : {{ props.name }}</p>
        <p>나이 : {{ props.age }}</p>
    </div>
</template>

<script setup>
    const props = defineProps({
        name: String,
        age: Number,
    })
</script>