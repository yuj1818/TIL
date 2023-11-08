<template>
    <div>
        <h3>이름 : {{ props.info.name }}</h3>
        <p>직함 : {{  props.info.title }}</p>
        <button @click="deleteCardFunc">명함 삭제</button>
    </div>
</template>

<script setup>
    const props = defineProps({
        info: Object
    })

    const emit = defineEmits(['deleteCardEvent'])

    const deleteCardFunc = () => {
        emit('deleteCardEvent', props.info)
    }

</script>

<style scoped>
    div {
        border: 1px solid lightgray;
        text-align: center;
        width: 40%;
        background-color: gainsboro;
        padding: 1rem;
    }
</style>