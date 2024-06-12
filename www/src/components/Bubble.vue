<script lang="ts" setup>
	withDefaults(defineProps<{
		variant: "solid" | "border";
		showDot: boolean;
	}>(), {
		variant: "solid",
		showDot: false
	})
</script>

<template>
	<div style="$attrs.style" :class="['bubble', {'border': variant === 'border'}]">
		<span v-if="showDot" class="bubble_dot"></span>
		<span class="bubble_text">
			<slot />
		</span>
	</div>
</template>

<style lang="scss">
	@import "@/assets/scss/_variables.scss";

	.bubble {
		position: relative;
		width: max-content;
		background: white;
		padding: 7px 15px;
		border-radius: 15px;
		border: 2px solid black;
		box-shadow: 3px 5px black;

		&.border {
			background-color: $base;
		}

		&_text {
			font-size: 14px;
			font-weight: bolder;
		}

		&_dot {
			position: absolute;
			right: 5px;
			top: -8px;
			width: 15px;
			height: 15px;
			border-radius: 100%;
			background: $base;
			border: 2px solid black;
		}
	}
</style>