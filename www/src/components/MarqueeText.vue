<script lang="ts" setup>
    import { ref, onMounted } from "vue";

    const containerRef = ref<HTMLDivElement | null>(null);

    onMounted(() => {
        if (!containerRef.value) return;
        
        const containerWidth = containerRef.value.getBoundingClientRect().width;
        const documentWidth = document.body.getBoundingClientRect().width;

        const marqueeText = containerRef.value.firstChild;
        const range = Math.round(documentWidth / containerWidth) + 1; // +1 to get correct no:of elements
        if (marqueeText) {
            for (let i = 0; i < range; i++) {
                containerRef.value.appendChild(marqueeText.cloneNode(true))
            }
        }
    })
</script>

<template>
    <div class="scroll_title" ref="containerRef">
        <h2>moonlit grace</h2>
    </div>
</template>

<style lang="scss">
    .scroll_title {
        position: absolute;
        left: 0;
        transform: translateY(-175px);
        display: flex;

        h2 {
            font-family: "Barlow Condensed", sans-serif;
            font-size: 250px;
            text-transform: uppercase;
            white-space: nowrap;
            position: relative;
            padding-right: 100px;
            user-select: none;
            // animation: marquee 20s linear infinite;

            &::after {
                position: absolute;
                left: 20px;
                top: 20px;
                content: "moonlit grace";
                text-transform: uppercase;
                font-size: 250px;
                color: transparent;
                -webkit-text-stroke: 2px rgba(0,0,0,0.5);
            }
        }
    }

    @keyframes marquee {
        0% {
            transform: translateX(0);
        }
        100% {
            transform: translateX(-100%);
        }
    }
</style>