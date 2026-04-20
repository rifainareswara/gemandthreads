<script>
  import { page } from '$app/state';

  const isHome = $derived(page.url.pathname === '/');
</script>

<!-- Bottom Navigation Bar - Mobile Only (from code2.html) -->
<nav class="md:hidden fixed bottom-0 left-0 w-full z-50 flex justify-around items-center px-4 pb-6 pt-2 bg-white/80 backdrop-blur-2xl rounded-t-[32px] shadow-[0px_-8px_24px_rgba(128,83,76,0.05)]">
  <!-- Home -->
  <a
    class="flex flex-col items-center justify-center p-3 rounded-full transition-all duration-300 {isHome ? 'bg-gradient-to-br from-primary to-primary-container text-white scale-100' : 'text-stone-400 hover:bg-stone-100'}"
    href="/"
  >
    <span class="material-symbols-outlined" style={isHome ? "font-variation-settings: 'FILL' 1;" : ""}>home</span>
  </a>

  <!-- Moods -->
  <a class="flex flex-col items-center justify-center text-stone-400 p-3 hover:bg-stone-100 rounded-full transition-colors" href="#moods">
    <span class="material-symbols-outlined">glass_cup</span>
    <span class="font-label text-[10px] tracking-widest uppercase mt-1">Moods</span>
  </a>

  <!-- Occasions -->
  <a class="flex flex-col items-center justify-center text-stone-400 p-3 hover:bg-stone-100 rounded-full transition-colors" href="#occasions">
    <span class="material-symbols-outlined">blanket</span>
    <span class="font-label text-[10px] tracking-widest uppercase mt-1">Occasions</span>
  </a>

  <!-- Cart -->
  <a class="flex flex-col items-center justify-center text-stone-400 p-3 hover:bg-stone-100 rounded-full transition-colors relative" href="/">
    <span class="material-symbols-outlined">shopping_basket</span>
    <span class="font-label text-[10px] tracking-widest uppercase mt-1">Cart</span>
    <span class="absolute top-2 right-2 w-2 h-2 bg-primary rounded-full"></span>
  </a>
</nav>
