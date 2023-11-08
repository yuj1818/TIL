<template>
    <div>
        <h3>자식 페이지입니다.</h3>
        <p>이름 : {{ props.child.name }}</p>
        <p>나이 : {{ props.child.age }}</p>
        <p>용돈 : {{ props.child.balance }}</p>
        <button @click="giveMeAllowance">용돈 주세요.</button>
    </div>
</template>

<script setup>
    const props = defineProps({
        child:Object,
    })
    
    // const { name, age, balance} = props

    const emit = defineEmits(['giveMeAllowance'])

    const giveMeAllowance = () => {
        emit('giveMeAllowance', props.child)
    }
</script>