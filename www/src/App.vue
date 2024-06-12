<script lang="ts" setup>
import MainCard from '@/components/MainCard.vue';
import MarqueeText from "@/components/MarqueeText.vue"
import SocialBtns from '@/components/SocialBtns.vue';
import Badges from "@/components/Badges.vue";

import { getTime } from "@/functions/time";
</script>

<template>
    <main>
        <MarqueeText />
        <div class="main_container">
            <div class="time">
                <span>{{ getTime() }}</span>
            </div>
            <MainCard />
            <div class="right_section_box">
                <SocialBtns />
                <Badges />
            </div>
        </div>
    </main>
</template>

<style lang="scss">
    @import "@/assets/scss/_variables.scss";

    main {
        width: 100dvw;
        height: 100dvh;
        background: url(assets/vectors/bg.svg);
        background-size: cover;
        background-position: top;
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        overflow: hidden;
    }

    .main_container {
        height: 575px;
        width: 400px;
        position: relative;

        @media screen and (max-width: 1024px) {
            display: flex;
            flex-direction: column;
            gap: 40px;
            height: 90%;
            width: 85%;
        }
    }

    .time {
        position: absolute;
        right: 375px;
        bottom: 125px;
        user-select: none;

        @media screen and (max-width: 1024px) {
            top: -120px;
            left: 0;
            right: 0;
            margin-left: auto;
            margin-right: auto;
            width: max-content;
            height: max-content;
        }

        span {
            font-family: "Barlow Condensed", sans-serif;
            font-size: 200px;
            color: $base;
            position: relative;
            -webkit-text-stroke: 3px black;
            text-shadow: 10px 15px black;

            @media screen and (max-width: 1024px) {
                font-size: 150px;
            }
        }
    }

    .right_section_box {
        position: absolute;
        top: 270px;
        left: 430px;
        z-index: 999;
        max-width: 300px;
        width: 100%;
        display: flex;
        flex-direction: column;
        gap: 30px;

        @media screen and (max-width: 1024px) {
            position: static;
        }
    }
</style>