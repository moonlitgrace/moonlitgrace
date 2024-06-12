<script lang="ts" setup>
import { EllipsisVertical, Heart, MessageCircle, Send, Bookmark } from 'lucide-vue-next';
import Bubble from './Bubble.vue';
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
			<span>108 likes</span>
			<p>lighted by the moon.</p>
			<span>View all 15 comments</span>
		</div>
		<!-- Bubbles -->
		<div class="bubbles">
			<Bubble :show-dot="true">hey there!</Bubble>
			<Bubble>I'm bored, let's have a chat?</Bubble>
		</div>
	</div>
</template>

<style lang="scss">
	@import "@/assets/scss/_variables.scss";

	.main_card {
		z-index: 100;
		height: 575px;
		width: 400px;
		position: relative;

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
				font-size: 14px;
			}

			svg {
				margin-left: auto;
				width: 20px;
				height: 20px;
			}
		}

		&_middle {
			border-radius: 15px;
			width: 100%;
			height: 100%;
			object-fit: cover;
			border: 2px solid black;
		}

		&_bottom {
			display: flex;
			flex-direction: column;
			gap: 6px;

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

			span {
				font-size: 12px;
				user-select: none;
			}

			p {
				font-size: 14px;
			}

			span:last-of-type {
				opacity: 0.5;
			}
		}
	}

	.bubbles {
		position: absolute;
		left: -125px;
		bottom: 135px;
		display: flex;
		flex-direction: column;
		gap: 10px;
		align-items: end;

		div:first-child {
			transform: translateX(-20px);
		}
	}
</style>