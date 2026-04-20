<script>
  import { onMount } from 'svelte';
  import { page } from '$app/state';
  import { fetchProduct, fetchProducts } from '$lib/api.js';
  import ProductCard from '$lib/components/ProductCard.svelte';

  let product = $state(null);
  let relatedProducts = $state([]);
  let loading = $state(true);
  let error = $state(null);

  const productId = $derived(Number(page.params.id));

  onMount(async () => {
    try {
      product = await fetchProduct(productId);
      // Fetch related products (same category, exclude current)
      const data = await fetchProducts(product.category);
      relatedProducts = data.products.filter(p => p.id !== product.id).slice(0, 4);
    } catch (e) {
      error = e.message;
      console.warn('Could not fetch product:', e.message);
    } finally {
      loading = false;
    }
  });
</script>

<svelte:head>
  {#if product}
    <title>{product.name} | Gem & Threads</title>
    <meta name="description" content={product.description} />
  {:else}
    <title>Product | Gem & Threads</title>
  {/if}
</svelte:head>

{#if loading}
  <!-- Loading Skeleton -->
  <div class="max-w-7xl mx-auto px-6 animate-pulse">
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-16">
      <div class="lg:col-span-7">
        <div class="aspect-[4/5] bg-surface-container-low rounded-2xl"></div>
      </div>
      <div class="lg:col-span-5 space-y-6">
        <div class="h-6 bg-surface-container-high rounded w-1/3"></div>
        <div class="h-12 bg-surface-container-high rounded w-3/4"></div>
        <div class="h-8 bg-surface-container-high rounded w-1/4"></div>
        <div class="h-24 bg-surface-container-high rounded"></div>
        <div class="h-14 bg-surface-container-high rounded-full"></div>
      </div>
    </div>
  </div>
{:else if error}
  <div class="text-center py-32 max-w-md mx-auto">
    <span class="material-symbols-outlined text-6xl text-stone-300 mb-4">error_outline</span>
    <h2 class="font-headline text-2xl mb-2">Product Not Found</h2>
    <p class="text-stone-500 mb-8">Start the backend server to load product data.</p>
    <a href="/" class="inline-flex items-center gap-2 bg-primary text-on-primary rounded-full px-8 py-3 font-label text-xs tracking-widest uppercase">
      <span class="material-symbols-outlined text-sm">arrow_back</span>
      Back to Shop
    </a>
  </div>
{:else if product}
  <div class="max-w-7xl mx-auto px-6">
    <!-- Breadcrumbs -->
    <nav class="mb-8 md:mb-12 flex items-center gap-2 text-xs tracking-widest uppercase text-outline">
      <a class="hover:text-primary transition-colors" href="/">Shop</a>
      <span class="material-symbols-outlined text-[10px]">chevron_right</span>
      <span class="text-stone-400">{product.category === 'jewelry' ? 'Jewelry' : 'Crochet'}</span>
      <span class="material-symbols-outlined text-[10px]">chevron_right</span>
      <span class="text-primary font-semibold">{product.name}</span>
    </nav>

    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-16 items-start">
      <!-- Product Gallery -->
      <div class="lg:col-span-7">
        <div class="relative overflow-hidden rounded-2xl bg-surface-container-low aspect-[4/5] mb-4">
          <img
            alt={product.name}
            class="w-full h-full object-cover"
            src={product.image_url}
          />
          <div class="absolute inset-0 crochet-overlay pointer-events-none"></div>
        </div>
      </div>

      <!-- Product Details -->
      <div class="lg:col-span-5 lg:sticky lg:top-32 space-y-6 md:space-y-8">
        <div class="space-y-4">
          <span class="inline-block px-4 py-1 rounded-full bg-secondary-container text-on-secondary-container text-[10px] font-bold tracking-[0.1em] uppercase">
            {product.category === 'jewelry' ? 'Crystal Jewelry' : 'Artisan Crochet'}
          </span>
          <h1 class="text-4xl md:text-5xl font-headline font-bold text-on-surface leading-[1.1] -tracking-[0.02em]">{product.name}</h1>
          <p class="text-2xl md:text-3xl font-headline italic text-primary">${product.price.toFixed(2)}</p>
        </div>

        <div class="space-y-6">
          <p class="text-on-surface-variant leading-relaxed font-body">{product.description}</p>

          <!-- Product Meta -->
          <div class="flex items-center gap-4 text-sm text-outline flex-wrap">
            {#if product.materials}
              <span class="flex items-center gap-1">
                <span class="material-symbols-outlined text-sm">eco</span>
                {product.materials}
              </span>
            {/if}
            {#if product.mood}
              <span class="w-1 h-1 rounded-full bg-outline-variant"></span>
              <span class="flex items-center gap-1">
                <span class="material-symbols-outlined text-sm">auto_awesome</span>
                Mood: {product.mood}
              </span>
            {/if}
          </div>
        </div>

        <!-- Stock Status -->
        <div class="flex items-center gap-2 text-sm">
          {#if product.stock > 5}
            <span class="w-2 h-2 rounded-full bg-green-500"></span>
            <span class="text-green-700">In Stock ({product.stock} available)</span>
          {:else if product.stock > 0}
            <span class="w-2 h-2 rounded-full bg-amber-500"></span>
            <span class="text-amber-700">Only {product.stock} left</span>
          {:else}
            <span class="w-2 h-2 rounded-full bg-red-500"></span>
            <span class="text-red-700">Out of Stock</span>
          {/if}
        </div>

        <!-- CTA Buttons -->
        <div class="pt-4 flex flex-col gap-4">
          <button class="w-full h-14 rounded-full bg-primary text-on-primary font-bold tracking-wide transition-all duration-300 hover:shadow-[0px_12px_32px_rgba(128,83,76,0.15)] hover:scale-[1.02] flex items-center justify-center gap-2 group">
            Add to Cart
            <span class="material-symbols-outlined text-xl group-hover:translate-x-1 transition-transform">arrow_right_alt</span>
          </button>
          <button class="w-full h-14 rounded-full border border-outline-variant text-on-surface font-semibold hover:bg-surface-container-low transition-colors flex items-center justify-center gap-2">
            <span class="material-symbols-outlined">favorite</span>
            Save to Wishlist
          </button>
        </div>
      </div>
    </div>

    <!-- Related Products -->
    {#if relatedProducts.length > 0}
      <section class="mt-24 md:mt-40 mb-16">
        <div class="flex justify-between items-end mb-8">
          <div>
            <h2 class="text-3xl md:text-4xl font-headline font-bold text-on-surface">Complementary Threads</h2>
            <p class="text-on-surface-variant mt-2 italic">Pairs beautifully with your artisanal choice.</p>
          </div>
          <a class="text-primary font-bold text-sm tracking-widest uppercase border-b-2 border-primary-fixed-dim pb-1 hover:text-primary-container transition-colors hidden sm:block" href="/">Explore All</a>
        </div>

        <div class="grid grid-cols-2 md:grid-cols-4 gap-6 md:gap-8">
          {#each relatedProducts as related, i}
            <div class={i % 2 === 1 ? 'translate-y-6' : ''}>
              <ProductCard product={related} />
            </div>
          {/each}
        </div>
      </section>
    {/if}
  </div>

  <!-- Mobile Bottom Action Bar -->
  <div class="lg:hidden fixed bottom-0 left-0 right-0 z-40 px-6 pb-8 pt-4 bg-white/80 backdrop-blur-2xl rounded-t-xl shadow-[0px_-8px_24px_rgba(128,83,76,0.05)]">
    <div class="max-w-md mx-auto flex items-center gap-4">
      <button class="p-4 rounded-full bg-surface-container text-primary flex items-center justify-center transition-all duration-300 hover:bg-stone-100">
        <span class="material-symbols-outlined">favorite</span>
      </button>
      <button class="flex-1 py-4 bg-gradient-to-br from-primary to-primary-container text-white rounded-full font-label text-sm tracking-widest uppercase font-bold shadow-[0px_12px_32px_rgba(128,83,76,0.15)] active:scale-95 transition-all duration-200">
        Add to Bag
      </button>
    </div>
  </div>
{/if}
