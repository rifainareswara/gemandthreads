<script>
  /** @type {{ product: { id: number, name: string, price: number, image_url: string, category: string, mood?: string } }} */
  let { product } = $props();
</script>

<a href="/products/{product.id}" class="group block">
  <div class="relative bg-surface-container-low rounded-2xl overflow-hidden mb-3 custom-shadow transition-all duration-300 group-hover:scale-[1.02] group-hover:-translate-y-1 group-hover:shadow-[0px_20px_40px_rgba(128,83,76,0.12)]">
    <div class="aspect-[3/4] overflow-hidden">
      <img
        src={product.image_url}
        alt={product.name}
        class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700"
        loading="lazy"
      />
    </div>
    <!-- Favorite Button -->
    <button
      class="absolute top-4 right-4 bg-white/80 backdrop-blur rounded-full p-2 text-primary opacity-0 translate-y-2 group-hover:opacity-100 group-hover:translate-y-0 transition-all duration-300"
      onclick={(e) => { e.preventDefault(); e.stopPropagation(); }}
    >
      <span class="material-symbols-outlined text-lg">favorite</span>
    </button>
    <!-- Category Badge -->
    {#if product.mood}
      <div class="absolute bottom-4 left-4 bg-white/80 backdrop-blur rounded-full px-3 py-1 opacity-0 group-hover:opacity-100 transition-opacity duration-300">
        <span class="text-[10px] tracking-widest uppercase font-label font-semibold text-primary">{product.mood}</span>
      </div>
    {/if}
  </div>
  <h3 class="font-body text-sm font-semibold text-on-background">{product.name}</h3>
  <div class="flex items-center gap-2 mt-1">
    <span class="text-primary font-semibold text-sm">${product.price.toFixed(2)}</span>
    <span class="text-[10px] tracking-widest uppercase text-stone-400 font-label">{product.category}</span>
  </div>
</a>
