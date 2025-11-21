<script lang="ts">
	import './layout.css';
	import favicon from '$lib/assets/favicon.svg';
	import { ModeWatcher } from "mode-watcher";
	import ThemeSwitcher from '$lib/components/themeswitcher.svelte';
	let { children } = $props();
</script>

<svelte:head>
	<!-- <link rel="icon" href={favicon} /> -->
	<title>lutra</title>
</svelte:head>

<ModeWatcher />
<header class="p-5 flex justify-end">
	<ThemeSwitcher />
</header>
{@render children()}
