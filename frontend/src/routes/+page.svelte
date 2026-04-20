<script>
  import { onMount } from 'svelte';
  import { fetchProducts } from '$lib/api.js';
  import Hero from '$lib/components/Hero.svelte';
  import ProductCard from '$lib/components/ProductCard.svelte';
  import ShopByMood from '$lib/components/ShopByMood.svelte';
  import ShopByOccasion from '$lib/components/ShopByOccasion.svelte';
  import InstagramFeed from '$lib/components/InstagramFeed.svelte';

  let products = $state([]);
  let loading = $state(true);
  let error = $state(null);

  onMount(async () => {
    try {
      const data = await fetchProducts();
      products = data.products;
    } catch (e) {
      error = e.message;
      // Fallback: use empty array, the page still renders with static sections
      console.warn('Could not fetch products from API:', e.message);
    } finally {
      loading = false;
    }
  });

  // Featured product for the bento card (first product)
  const featured = $derived(products[0]);
  // Grid products (skip first, take next 2)
  const gridProducts = $derived(products.slice(1, 3));
  // Crochet promo product
  const crochetProducts = $derived(products.filter(p => p.category === 'crochet'));
</script>

<svelte:head>
  <title>Gem & Threads | Handcrafted Jewelry & Crochet</title>
  <meta name="description" content="Handcrafted crystal jewelry and artisanal crochet threads, woven together for moments of mindful elegance." />
</svelte:head>

<!-- Hero Section -->
<Hero />

<!-- New Arrivals: Bento Grid -->
<section id="arrivals" class="max-w-7xl mx-auto px-6 mb-24 md:mb-32">
  <div class="flex justify-between items-end mb-12">
    <div>
      <span class="font-label text-xs tracking-[0.1em] uppercase text-primary mb-2 block">New Arrivals</span>
      <h2 class="font-headline text-3xl md:text-4xl">Latest Creations</h2>
    </div>
    <a class="text-primary font-medium underline underline-offset-8 decoration-primary-fixed-dim hidden sm:block" href="#arrivals">Explore All</a>
  </div>

  {#if loading}
    <!-- Loading Skeleton -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-6">
      {#each Array(4) as _}
        <div class="bg-surface-container-low rounded-2xl p-6 animate-pulse">
          <div class="aspect-square bg-surface-container-high rounded-xl mb-4"></div>
          <div class="h-4 bg-surface-container-high rounded w-3/4 mb-2"></div>
          <div class="h-3 bg-surface-container-high rounded w-1/2"></div>
        </div>
      {/each}
    </div>
  {:else if error}
    <!-- Error State -->
    <div class="text-center py-16">
      <span class="material-symbols-outlined text-5xl text-stone-300 mb-4">cloud_off</span>
      <p class="text-stone-500">Unable to load products. Start the backend server to see live data.</p>
      <p class="text-xs text-stone-400 mt-2">{error}</p>
    </div>
  {:else}
    <div class="grid grid-cols-1 md:grid-cols-4 gap-6">
      <!-- Featured Large Product -->
      {#if featured}
        <a href="/products/{featured.id}" class="md:col-span-2 md:row-span-2 bg-surface-container-low rounded-2xl p-8 group overflow-hidden block">
          <div class="h-[300px] md:h-[400px] mb-6 rounded-xl overflow-hidden relative">
            <img
              class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700"
              alt={featured.name}
              src={featured.image_url}
              loading="lazy"
            />
          </div>
          <h3 class="font-headline text-2xl mb-2">{featured.name}</h3>
          <p class="text-on-surface-variant mb-4">{featured.description}</p>
          <span class="text-primary font-bold">${featured.price.toFixed(2)}</span>
        </a>
      {/if}

      <!-- Grid Products -->
      {#each gridProducts as product}
        <div class="bg-surface-container-low rounded-2xl p-6 group">
          <a href="/products/{product.id}">
            <div class="aspect-square mb-4 rounded-xl overflow-hidden">
              <img
                class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700"
                alt={product.name}
                src={product.image_url}
                loading="lazy"
              />
            </div>
            <h4 class="font-medium text-lg">{product.name}</h4>
            <span class="text-stone-500">${product.price.toFixed(2)}</span>
          </a>
        </div>
      {/each}

      <!-- Crochet Promo Banner -->
      <div class="md:col-span-2 bg-secondary-container/30 rounded-2xl p-8 flex items-center gap-8 relative overflow-hidden">
        <div class="crochet-overlay absolute inset-0"></div>
        <div class="relative z-10 max-w-xs">
          <h3 class="font-headline text-2xl md:text-3xl mb-4">Artisan Woven Totes</h3>
          <p class="text-sm text-on-secondary-container mb-6">Sustainable fibers hand-knotted by our community of makers.</p>
          <button class="bg-white text-on-background rounded-full px-6 py-2 font-label text-[10px] tracking-widest uppercase hover:shadow-md transition-shadow">View Series</button>
        </div>
        <div class="relative z-10 h-full hidden sm:block">
          <img
            class="h-48 w-48 object-cover rounded-full shadow-lg"
            alt="Large textured beige crochet tote bag"
            src="https://lh3.googleusercontent.com/aida-public/AB6AXuBieBPcDUr6DHw45W2OwCJl_fPVbZ7jXKuzjeZsuRXTtwVWdVIo23Ut5NUvnQJMff0cBJF56Rg5aWv6pbOpZlE_rA4TZ7SF_eslFlsqb8UL18GgPbPnSmsUxgvtpSbwrcM3hKN0WM7Aaui2CvjRdHHJ_J05W2ZX-5kgDV3pdcNR6zDJ_J14Csd2dPZ2H7g8D9YHQjp858Tdiqdd6PwTqqDBrqkrxDQpW90-GPozy42F4ck0tFQF1-fHZFcRJ4sfQO3TjvPN1B46U_VQ"
            loading="lazy"
          />
        </div>
      </div>
    </div>

    <!-- Full Product Grid -->
    <div class="mt-16">
      <h3 class="font-headline text-2xl mb-8">All Products</h3>
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-x-6 gap-y-10">
        {#each products as product}
          <ProductCard {product} />
        {/each}
      </div>
    </div>
  {/if}
</section>

<!-- Shop by Mood -->
<ShopByMood />

<!-- Shop by Occasion -->
<ShopByOccasion />

<!-- Instagram Feed -->
<InstagramFeed />
