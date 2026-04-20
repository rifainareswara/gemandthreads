<script>
  const images = [
    { src: "https://lh3.googleusercontent.com/aida-public/AB6AXuD2Wq0c_ruU5Gnv-njD9uYhpiVZuOgYNuUGK4sNNdxm5GTYeZNe2OxhA7MkSRElhiuO2ry95ahHHQagaDVUleEIalFf_sHTxvckLo_EA3PgydREVzZChPFZ_GloUqkUPWUzm0G4BVXNGiR44aCW94Wln3LyFXrPNJ4bI7ei_kcKRb56Ut4oKCQQY1mBFq-P78RRK2iu_wdvy4kxiIr2LVQZ0JHh_VQ3PDFXbF1ql98oVnYnPAGt-UCBeoYVtn_jyFXS75kAn6t8e3DA", alt: "Customer wearing jewelry in a cozy coffee shop" },
    { src: "https://lh3.googleusercontent.com/aida-public/AB6AXuDmoFDH--FOVjQVpze63SWIzitmZ8W86eFHwhEKvfG51_G68_WjyKG1qgwaLyzgTpdputUg2aC2iJEfFJq_9R-p1ajOOSs9IUKZ2BwNWp91AKg0XxWrP4_aGFvbs8MA-zLxXLoi519oIam10vGfa6RtEb4hbcRhFHHBw9WNb1EWSFxgOJ_EBBSaqNQATX_KRDYISbXHpzJulf_CrUAzw5QfkLpK20wclELcWNhYOZHfZIjd5tqnyMwuXl7hNTdl5iQzWvqqp6eqHc36", alt: "Jewelry being packaged in sustainable box" },
    { src: "https://lh3.googleusercontent.com/aida-public/AB6AXuBEzxF96SDLYDxA_KOQ4WM33gModCa1mtwZbIgxNVtU9ZV3bgUQj_1Us-748QIvggku7UkAq3eaeB92_H9YJPm3bd4iag-tH97LpboDOML_Ml72alDten4UaDXIgtzGOz3_9KrNqHS7YAPHXVSX-g8gsPDyifBLM7iexlQmU-YGoxCerG4q3q72n5_6sCHMuj2gPSjaoXTP0HDPrfgg50rmiSOAMeQdneIKOTMZE_M8MnxKB1l_MW30Uo7cpeHL19QKh1N_fE6gacQa", alt: "Flat lay of artisan tools, crystals, and threads" },
    { src: "https://lh3.googleusercontent.com/aida-public/AB6AXuC6m7ASLySAlVVJNmlXLW_1PdxKy1bLh2N6kvau8qaY5N-QvTLIZRe0XhhHWzjnv5UP8deCPnE_J0Hbrs_D_lQOIuixcoYpQ5VvoFAHl1CZSlcA06MjjHDM76F1nsIS-POJOHvcrPJYrj-eKhBvUs7cBvLC6QqUmBWMSoz7QWYUjjS2Fd-gQG8mf5DPIQ1Ci8MGzEvwRk8uTuXcEro0PkGsfzHZPjV8IFe4IPgbWMwqLgO-sul3KZlbvkwtNxaJuSYlAHod66Vhymat", alt: "Person crocheting a colorful bag in a sunlit garden" },
    { src: "https://lh3.googleusercontent.com/aida-public/AB6AXuCgBkUGzU9k4J4Kkp2ICWPM_cVYF3FQmRCCe1XyQRxkAe87xk-eqhTBO4ZHmrHQnOqis50ctUuxPlQAX9cCwTZAuWBTklEOeKAcmXImeXV8HdOZxGZfThs0QAjo4y_1_Opqb8FHW7UrBnfKJdoRGGScACeV7J7LTFmy1EWUPLBRizsIVpEloU0by4kkQAMq9xylLcxz1e4AicpL2aPs9B1T76goq6HoA606kAaynVxeAlXCpnAtW8JeEg1gjnZJ1tRDzOgpWiSSmbc0", alt: "Incense smoke swirling over jewelry" },
    { src: "https://lh3.googleusercontent.com/aida-public/AB6AXuCNgFSEB66ls3renzNR1TA2hT2g0vpszfaicvp4MZUqvyjaIHZsIvMxYoFfJ7fcREpjUdw8ON0FgZf3UzRygcbgS-osa9PCmxbyPb5SKlGLYLEzpKGVFV4ZLHEM9Hl2_Mj3nLO-_CfbxmG11lp_gOvwxuSJZchBt8jDhLe2Y6LEn9vns-rMPwshVXJtXOqv8iKEbbxCf-3bRhZ3WMrFBwFw5sdy4efCPVSiJ21XSKrX0wAk1fYAwj7viFhd1wZJD6EMo5YcQs98b5cM", alt: "Outfit of the day featuring artisan crochet accessories" },
  ];
</script>

<!-- Instagram Feed Section (from code.html) -->
<section class="max-w-7xl mx-auto px-6 mb-24 md:mb-32">
  <div class="text-center mb-12">
    <span class="font-label text-xs tracking-[0.1em] uppercase text-primary mb-2 block">Community</span>
    <h2 class="font-headline text-3xl">@GemAndThreads</h2>
  </div>

  <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-2">
    {#each images as image}
      <div class="aspect-square bg-surface-container overflow-hidden group cursor-pointer">
        <img
          class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700"
          alt={image.alt}
          src={image.src}
          loading="lazy"
        />
      </div>
    {/each}
  </div>
</section>
