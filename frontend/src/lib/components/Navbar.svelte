<script>
  let mobileMenuOpen = $state(false);
</script>

<!-- TopAppBar -->
<header class="fixed top-0 left-0 right-0 z-50 flex justify-between items-center h-16 bg-white/70 backdrop-blur-xl rounded-full mt-4 mx-auto max-w-7xl px-6 shadow-[0px_12px_32px_rgba(128,83,76,0.08)]">
  <a href="/" class="text-2xl font-headline tracking-tight text-primary">Gem & Threads</a>

  <!-- Desktop Nav -->
  <nav class="hidden md:flex items-center gap-8">
    <a class="text-primary font-semibold border-b-2 border-primary-fixed-dim pb-1 font-label text-xs tracking-[0.05em] uppercase" href="/">Shop</a>
    <a class="text-stone-500 font-medium hover:text-primary transition-colors duration-300 font-label text-xs tracking-[0.05em] uppercase" href="#moods">Moods</a>
    <a class="text-stone-500 font-medium hover:text-primary transition-colors duration-300 font-label text-xs tracking-[0.05em] uppercase" href="#occasions">Occasions</a>
    <a class="text-stone-500 font-medium hover:text-primary transition-colors duration-300 font-label text-xs tracking-[0.05em] uppercase" href="#about">About</a>
  </nav>

  <div class="flex items-center gap-5">
    <button class="hover:scale-95 transition-transform duration-200 ease-out text-primary hidden md:block">
      <span class="material-symbols-outlined">search</span>
    </button>
    <button class="hover:scale-95 transition-transform duration-200 ease-out text-primary">
      <span class="material-symbols-outlined">shopping_bag</span>
    </button>
    <button class="hover:scale-95 transition-transform duration-200 ease-out text-primary hidden md:block">
      <span class="material-symbols-outlined">favorite</span>
    </button>
    <button class="hover:scale-95 transition-transform duration-200 ease-out text-primary hidden md:block">
      <span class="material-symbols-outlined">person</span>
    </button>
    <!-- Mobile Menu Toggle -->
    <button class="md:hidden hover:scale-95 transition-transform duration-200 ease-out text-primary" onclick={() => mobileMenuOpen = !mobileMenuOpen}>
      <span class="material-symbols-outlined">{mobileMenuOpen ? 'close' : 'menu'}</span>
    </button>
  </div>
</header>

<!-- Mobile Menu Overlay -->
{#if mobileMenuOpen}
  <div class="fixed inset-0 z-40 bg-white/95 backdrop-blur-xl pt-24 px-8 md:hidden" role="dialog" aria-label="Mobile navigation">
    <nav class="flex flex-col gap-6">
      <a class="text-primary font-headline text-3xl" href="/" onclick={() => mobileMenuOpen = false}>Shop</a>
      <a class="text-stone-500 font-headline text-3xl hover:text-primary transition-colors" href="#moods" onclick={() => mobileMenuOpen = false}>Moods</a>
      <a class="text-stone-500 font-headline text-3xl hover:text-primary transition-colors" href="#occasions" onclick={() => mobileMenuOpen = false}>Occasions</a>
      <a class="text-stone-500 font-headline text-3xl hover:text-primary transition-colors" href="#about" onclick={() => mobileMenuOpen = false}>About</a>
    </nav>
  </div>
{/if}
