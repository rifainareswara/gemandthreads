"""
Mock in-memory database for Gem & Threads.
Pre-populated with products extracted from the HTML mockups.
"""

from typing import Optional
from app.models import Product, Category


PRODUCTS: list[Product] = [
    Product(
        id=1,
        name="Aura Crystal Collection",
        description="Cleansed with sage, charged with intention. A stunning layered necklace set featuring hand-selected crystals that radiate natural beauty and positive energy.",
        price=124.00,
        stock=12,
        category=Category.jewelry,
        image_url="https://lh3.googleusercontent.com/aida-public/AB6AXuACAFUgedjwo0gcTq5vpC1_P3x6hrh-ApV5jBJ3ioaiGMU6DoXOAPFhWaMf6FpOM48x4t73TohHiutBcKF4oZejgwKlpKGO-mOdFEtHHLhwUidzXFWuY1MdYrNCbNurm9vsUiBLJkT5nEkZXuXs7IEzxz6bPc5xAjCJ7oMk39LRfoK6OqShyxIwPUaDrHGqth0fMH-oe53T-s99nqgQmlzGMUO6vW0BsUG1lXid7v8fhMnRJUGu4ldGHFxnL5WXvscM9rl3KyReOjRO",
        mood="Calm",
        materials="Assorted Crystals, Sterling Silver Chain"
    ),
    Product(
        id=2,
        name="Emerald Knot Clutch",
        description="An intricate emerald green crochet clutch with gold-tone hardware, perfect for evening occasions or adding a pop of artisanal elegance.",
        price=85.00,
        stock=8,
        category=Category.crochet,
        image_url="https://lh3.googleusercontent.com/aida-public/AB6AXuDQA-RkrCshufOdm3DPnIw_6rNFX9kmBm4XkL0YwVu_FwPp3bQUikq44FwYcM_d3fVInX1VQnYSRZWl5F2RjMOTbi76by31wzvsloyiXgwXb4vSV6ZIUs4_1tQedhIFY--ahM9ez-FX5QVeMQMWxtlYpIKy-y36b2gI2o9uDfPMid2TFNXYrIoiZ89IdKgKhzyj3weNGuKepKT94u_Bp_zk7SFvNvKQEJ2G1fxdl34bYYSBPmlVxrni8SZJXYg3uUizblotKb6Woqqq",
        mood="Energetic",
        materials="Organic Cotton Thread, Gold-Tone Hardware"
    ),
    Product(
        id=3,
        name="Intuition Studs",
        description="Amethyst geode earrings resting on a white silk ribbon. These studs channel the mystical energy of amethyst, ideal for the spiritually aware.",
        price=45.00,
        stock=20,
        category=Category.jewelry,
        image_url="https://lh3.googleusercontent.com/aida-public/AB6AXuDNk884Q-3zBYg5wqauewoMEwPRC7L8M6sUoupIznRNC4KmnRA6kseZ3bXGNvaSlM_yrq8Z1B_gazAzfiRa1T7NNXaLT0GUQEM5N8cqq9PnOGGZQjR_l4N9f1ctCdLjmgBUPYg1ZqMBSDbsAElxTqArimAFM3k3YWXnAQRanboe54hnZ3hSnHhzF9dP3LK2YmAA7qUaJ5-AutFg0RvJvovmcKNqKgXt42Uuv9L2Ujwl9z2t48JyKCiY6oQZeVof40QgHLr7UPaaYf0F",
        mood="Calm",
        materials="Amethyst Geode, Sterling Silver"
    ),
    Product(
        id=4,
        name="Meadow Weave Cardigan",
        description="A cream-colored chunky knit crochet cardigan draped over a minimalist wooden chair. Comfortable, breathable, and beautifully textured.",
        price=124.00,
        stock=5,
        category=Category.crochet,
        image_url="https://lh3.googleusercontent.com/aida-public/AB6AXuCJJfr5idfw1zpUCV5m488r2SfAMzhrXHaXDeWEJWtLtcpFD3vaixT_Z7KLr4v-K-mWwHEnnAqWTzzZEOaWHGjy7KgETnOr3sbVV5txx-LpVJe_WbZP6RKgvXxsW-dk589x47Ri-0GT7YrB_MJcyre76hOhEc_FGzRyGCfTencw9GSYUf6xALr0RezoZ5mcUsM_e2HRWrxXUKtbuESxP0lZyw3AXMBOIOAj8BzfFWuBe8zK8aW2CYxHTVxAJJ7uLJRL2kIxWcRoK5FR",
        mood="Calm",
        materials="100% Organic Cotton"
    ),
    Product(
        id=5,
        name="Spirit Amethyst Charm",
        description="Amethyst and gold bead bracelet shimmering under soft diffused light. A wearable talisman that harmonizes your spirit with amethyst's soothing vibrations.",
        price=48.00,
        stock=15,
        category=Category.jewelry,
        image_url="https://lh3.googleusercontent.com/aida-public/AB6AXuDzsfIHvTBIPMNs-spfvn5rJHBVUjitl3EdhU21rPpXmWGMDcEQLbBiF4ish0OMiiewt6dVq_RewHfLc0dWBRSxu0RnPuekcl9IPKQoim3cvIxXh8EJWjXXje_pn9sPJpSI65PjO2NLdWBDrBPoEQ1AYSodiFfAzNR3yJxxS6Hi9V9_rlVZLQYMoHt2g_aIQBZ9pHzSZugKvgq8-43a49zKIBWz52GREURfVOuORMIJhQKY6rRc8OCmgm47k3yZm2oTzf4O6qNeSZ5U",
        mood="Romantic",
        materials="Amethyst, Gold-Plated Beads, Silk Thread"
    ),
    Product(
        id=6,
        name="Heirloom Lace Scarf",
        description="Intricate white lace pattern from a handcrafted vintage-style scarf. A timeless crochet masterpiece that adds delicate elegance to any outfit.",
        price=85.00,
        stock=7,
        category=Category.crochet,
        image_url="https://lh3.googleusercontent.com/aida-public/AB6AXuCBzSqA0qtSAtbc9S64IxUV3PYhdhgF2B0bizcp5xOFoV_6rZCZkIKldiWmmLtA6qIVxQV8l2ClF40X6WKKoHkKyeBE0lmxZFmgGFZDanypfnpuJdONtvisG_zHX3FdCCdYMCoqPIxwQHq_hMXkPw8deea4vttiTntGCxD2QD0_uCVqrsm5Cft-w5ToXpjSWkV0EsUDKu4oVOsbXuiqfDCDSteY4cBbBP8AvYDJWeQfZCEHFXFUg5W8yQm1y5t0Ibjp2lvZpO9nduYs",
        mood="Romantic",
        materials="Premium Lace Thread"
    ),
    Product(
        id=7,
        name="Zen Jade Mala",
        description="Smooth green jade meditation beads reflecting soft garden light. Perfect for mindful meditation or as a stunning wearable piece of serenity.",
        price=62.00,
        stock=10,
        category=Category.jewelry,
        image_url="https://lh3.googleusercontent.com/aida-public/AB6AXuASIVIRQznn1neTxRMebcfNPAHQBpqgWYBpQUgfxqwElED5_QSsRcRCVmEM54MUDXIXDsSXOLkjEn1n1BfbQ8YRoUp6VBwdUz3VBLcTF1VTwfHPqXBkHAXa337cEOiFG7acyznis7isiUFWilBoOXpjbQG-masq9DtU6vT5fHLT6mc9J3uB0YERHweVk7uDIwMHCKUA4TU_E4e-2AiHszgwbqkUgBsZgRgjrPo5l-JG2d5iL6HI7277vdSqnj3ux6Ie8zR7pHiuEbGz",
        mood="Calm",
        materials="Grade A Green Jade, Silk Cord"
    ),
    Product(
        id=8,
        name="Handcrafted Crochet Tote",
        description="Elevate your everyday with the 'Aria' tote. Each piece is meticulously hand-woven over 14 hours by our resident artisans, using sustainably sourced organic cotton.",
        price=285.00,
        stock=3,
        category=Category.crochet,
        image_url="https://lh3.googleusercontent.com/aida-public/AB6AXuAZ2QNFGwASEifgJ9HW5llEOdOVXrBG_qqAQMXApSGIC1vi4loHhvmD4NQ_Pa0NJLcJXCtJ3hqBTnU6HqpQJj5VzxUFAfkdxidEmknGOPp7mQXXiXKjl-aHSBegVoEkCiOm3YOZyda86itrfzYl3NOKjmGmX3t0MFUfreUxUPYxvJaSCQBywp7AKT7vQrsHO8GjXQujEJzU2_PVFG2AoDu-QavGjsj0zPZoDttYCsmvSpNwGqwk35FTbq8cuNnTAZQNWOtsRaRk2KUD",
        mood="Calm",
        materials="100% Organic Cotton, Double-Loop Stitch"
    ),
    Product(
        id=9,
        name="Amethyst Crystal Bracelet",
        description="Hand-knotted with silk threads and punctuated by hand-picked Amethyst clusters. Each piece reflects the unique geometry of the earth, designed to rest softly against your pulse point.",
        price=148.00,
        stock=6,
        category=Category.jewelry,
        image_url="https://lh3.googleusercontent.com/aida-public/AB6AXuCHItCA4PY6-3OOPgob7LJtOJqQOHwglcAcoHTIqzA6YW54pkHKFTLnFwnpWQoiOtqPlo4QO0zB4de08nqv6dYW5pXvfZkRIcrPxYTjHZPhCCohMlBZw69OCif5DIGKhD6doDakmuvaIMgBe2xzB5I-S0VyCSwg_VLThm9t7O6V2Hlu6xi4dJ1_dYAVVSUnMXRY0ygIY-1p6SjdivuRMUH702s-1wQj6W6hcMP06bNPZ2EqzQEEJ7r_IppS0QkF-7P9CdbYAWHhpZp2",
        mood="Calm",
        materials="Grade A Amethyst, Recycled 14k Gold, Silk Thread"
    ),
    Product(
        id=10,
        name="Artisan Woven Tote",
        description="Sustainable fibers hand-knotted by our community of makers. A large textured beige crochet tote bag perfect for everyday elegance.",
        price=195.00,
        stock=4,
        category=Category.crochet,
        image_url="https://lh3.googleusercontent.com/aida-public/AB6AXuBieBPcDUr6DHw45W2OwCJl_fPVbZ7jXKuzjeZsuRXTtwVWdVIo23Ut5NUvnQJMff0cBJF56Rg5aWv6pbOpZlE_rA4TZ7SF_eslFlsqb8UL18GgPbPnSmsUxgvtpSbwrcM3hKN0WM7Aaui2CvjRdHHJ_J05W2ZX-5kgDV3pdcNR6zDJ_J14Csd2dPZ2H7g8D9YHQjp858Tdiqdd6PwTqqDBrqkrxDQpW90-GPozy42F4ck0tFQF1-fHZFcRJ4sfQO3TjvPN1B46U_VQ",
        mood="Energetic",
        materials="Sustainable Natural Fibers"
    ),
    Product(
        id=11,
        name="Flora Silk Scarf",
        description="A delicate silk scarf with hand-painted floral motifs, perfect for adding artisan elegance to any ensemble.",
        price=120.00,
        stock=9,
        category=Category.crochet,
        image_url="https://lh3.googleusercontent.com/aida-public/AB6AXuBR3tOv_Ob_dsBGaJZr3U-Jl2PxQeBIXtAUg_P0_hxHPel348N3UEe9mre21ap1s2QuUsvYBsKu08yLdaCCsYg4czUENnopf42_iffuLkBmjFuweGgNargy6e8V1AFX8bGRJo9rsV4xn5K46DUd7-9-KXvaMC90QzuIwbLrZ5uPHYOdN_HcnNvxZ8AAMuP-jxjwIlBt08jc6XVJBNxNlx5bk2o4e4SaE3jo67NuGPqlgbMXTUoyuD23An-q4JC6vPuCUvc6t4fAff2p",
        mood="Romantic",
        materials="100% Mulberry Silk"
    ),
    Product(
        id=12,
        name="Quartz Solstice Ring",
        description="A rose gold ring set with a clear polished gemstone catching direct sunlight. A statement piece that captures the brilliance of nature.",
        price=420.00,
        stock=2,
        category=Category.jewelry,
        image_url="https://lh3.googleusercontent.com/aida-public/AB6AXuDubRr1ghKU6Fyow4qePIUzkaNzWob0Z-EgiePW47yzNjezN0YRnOyE5TORWs5t-IrGx5ldL0D2P3T4PEO-q7927XsYmB17EPLmosqJW0Tl3L9gUf_VAuHi17GjRsWp3aRKD2Gydqemf2Rermi5HWemdqtaIBletIgdwilcdteumCefj2-cXtUaJYnFCCuM6KgylUiDXfoNvaPyuKkI8Y6jYZzu6Zl14chH8qzUMJMxk7fakrZgzZDU_ZXyNoiJP0cyUKqr5gNQtosr",
        mood="Energetic",
        materials="Rose Gold, Clear Quartz"
    ),
]


def get_all_products() -> list[Product]:
    """Return all products."""
    return PRODUCTS


def get_product_by_id(product_id: int) -> Optional[Product]:
    """Return a single product by its ID, or None if not found."""
    for product in PRODUCTS:
        if product.id == product_id:
            return product
    return None


def get_products_by_category(category: str) -> list[Product]:
    """Return products filtered by category."""
    return [p for p in PRODUCTS if p.category.value == category]
