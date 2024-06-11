<script lang="ts" setup>
import MainCard from '@/components/MainCard.vue';
import MarqueeText from "@/components/MarqueeText.vue"
</script>

<template>
    <main>
        <MarqueeText />
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
    }
</style>