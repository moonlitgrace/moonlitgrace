<script lang="ts" setup>
import { EllipsisVertical, Heart, MessageCircle, Send, Bookmark } from 'lucide-vue-next';
</script>

<template>
	<div class="main_card">
		<div class="main_card_top">
			<img src="../assets/images/pfp.jpg">
			<span>moonligrace</span>
			<EllipsisVertical />
		</div>
		<img class="main_card_middle" src="../assets/images/main.jpg">
		<div class="main_card_bottom">
			<div class="card_options">
				<Heart />
				<MessageCircle />
				<Send />
				<Bookmark />
			</div>
			<div class="context">
				<span>108 likes</span>
				<p>lighted by the moon.</p>
				<span>View all 15 comments</span>
			</div>
		</div>
	</div>
</template>

<style lang="scss">
	@import "@/assets/scss/_variables.scss";

	.main_card {
		height: 575px;
		width: 400px;

		display: flex;
		flex-direction: column;
		gap: 10px;
		padding: 15px;
		background: white;
		border: 2px solid black;
		border-radius: 30px;
		box-shadow: 10px 15px black;

		&_top {
			display: flex;
			align-items: center;
			gap: 10px;

			img {
				width: 30px;
				height: 30px;
				border-radius: 100%;
				border: 2px solid black;
			}

			span {
				font-size: 12px;
			}

			svg {
				margin-left: auto;
				width: 20px;
				height: 20px;
			}
		}

		.main_card_middle {
			border-radius: 15px;
			width: 100%;
			height: 100%;
			object-fit: cover;
			border: 2px solid black;
		}

		&_bottom {
			display: flex;
			flex-direction: column;
			gap: 5px;

			.card_options {
				display: flex;
				align-items: center;
				gap: 10px;

				svg {
					width: 25px;
					height: 25px;
				}

				svg:first-child {
					fill: $base;
				}

				svg:last-child {
					margin-left: auto;
				}
			}

			.context {
				display: flex;
				flex-direction: column;
				gap: 0px;

				span {
					font-size: 12px;
				}

				p {
					font-size: 14px;
				}

				span:last-of-type {
					opacity: 0.5;
				}
			}
		}
	}
</style>