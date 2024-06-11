<script lang="ts" setup>
import MainCard from './components/MainCard.vue';
</script>

<template>
    <main>
        <MainCard />
    </main>
</template>

<style lang="scss">
    main {
        width: 100vw;
        height: 100vh;
        background: url(assets/vectors/bg.svg);
        background-size: cover;
        background-position: top;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
    }
</style>