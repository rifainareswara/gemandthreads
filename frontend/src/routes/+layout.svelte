<script>
  import './layout.css';
  import Navbar from '$lib/components/Navbar.svelte';
  import Footer from '$lib/components/Footer.svelte';
  import BottomNav from '$lib/components/BottomNav.svelte';

  let { children } = $props();
</script>

<svelte:head>
  <meta name="theme-color" content="#80534c" />
</svelte:head>

<Navbar />

<main class="pt-24 pb-24 md:pb-32">
  {@render children()}
</main>

<Footer />
<BottomNav />
