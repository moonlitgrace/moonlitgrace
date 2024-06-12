<script lang="ts" setup>
import Bubble from './Bubble.vue';

const mapping = ["coding", "designing", "drawing & painting"];
</script>

<template>
	<div class="badges_container">
		<template v-for="item in mapping">
			<Bubble variant="border">{{ item }}</Bubble>
		</template>
		<Bubble variant="border" style="user-select: none;">...</Bubble>
	</div>
</template>

<style lang="scss">
	.badges_container {
		display: flex;
		flex-wrap: wrap;
		gap: 15px;
		row-gap: 10px;
	}
</style>