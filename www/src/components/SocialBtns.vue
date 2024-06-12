<script lang="ts" setup>
import { h } from "vue";
import { siX, siDiscord, siGithub, siTelegram } from "simple-icons";

import GithubIcon from "@/components/icons/GithubIcon.vue";
import TwitterIcon from "@/components/icons/TwitterIcon.vue";
import TelegramIcon from "@/components/icons/TelegramIcon.vue";
import DiscordIcon from "@/components/icons/DiscordIcon.vue";

const mapping =  [
	{
		icon: GithubIcon,
		href: "/"
	},
	{
		icon: TwitterIcon,
		href: "/"
	},
	{
		icon: TelegramIcon,
		href: "/"
	},
	{
		icon: DiscordIcon,
		href: "/"
	}
];
</script>

<template>
	<div class="socials_container">
		<template v-for="item in mapping">
			<a :href="item.href">
				<component :is="item.icon" />
			</a>
		</template>
	</div>
</template>

<style lang="scss">
	.socials_container {
		display: grid;
		grid-template-columns: repeat(4, 1fr);
		gap: 20px;

		a {
			width: 100%;
			aspect-ratio: 1/1;
			display: grid;
			place-items: center;
			text-decoration: none;
			color: inherit;
            background: white;
            outline: none;
            border-radius: 15px;
            border: 2px solid black;
            box-shadow: 5px 10px black;
        }

		svg {
			width: 30px;
			height: 30px;
		}
	}
</style>