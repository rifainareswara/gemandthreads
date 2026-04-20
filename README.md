<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/Svelte-FF3E00?style=for-the-badge&logo=svelte&logoColor=white" alt="Svelte"/>
  <img src="https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white" alt="Tailwind CSS"/>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
</p>

<h1 align="center">💎🧶 Gem & Threads</h1>
<p align="center"><em>Handcrafted crystal jewelry and artisanal crochet threads, woven together for moments of mindful elegance.</em></p>

<p align="center">
  A full-stack boutique e-commerce web application built with <strong>FastAPI</strong> (Python) and <strong>SvelteKit</strong> (Svelte 5) + <strong>Tailwind CSS v4</strong>.
</p>

---

## 📋 Table of Contents

- [Features](#-features)
- [Screenshots](#-screenshots)
- [Tech Stack](#-tech-stack)
- [Architecture](#-architecture)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [API Documentation](#-api-documentation)
- [Design System](#-design-system)
- [Components](#-components)
- [Environment Variables](#-environment-variables)
- [Docker](#-docker)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🛍️ **Product Catalog** | Browse 12+ handcrafted jewelry and crochet products |
| 🔍 **Category Filtering** | Filter products by Jewelry or Crochet categories |
| 📱 **Responsive Design** | Desktop and mobile-optimized layouts with distinct UX |
| 🎭 **Shop by Mood** | Curated collections — Calm, Energetic, Romantic |
| 🎁 **Shop by Occasion** | Wedding, Casual, Gifting — themed product sets |
| 📄 **Product Detail Pages** | Full product pages with breadcrumbs, stock status, and related items |
| 📸 **Instagram Feed** | Community gallery section with hover zoom effects |
| ⚡ **Loading States** | Skeleton loaders and graceful error handling |
| 🎨 **Material Design 3** | Premium color palette with glassmorphism and micro-animations |
| 🐳 **Docker Ready** | One-command setup with Docker Compose |

---

## 📸 Screenshots

### Landing Page — Hero Section
> Glassmorphism navbar with serif typography and full-bleed hero image

![Hero Section](docs/screenshots/hero.png)

### Product Grid — API Powered
> Bento-style grid layout with featured product, category cards, and promo banner

![Product Grid](docs/screenshots/products.png)

### Product Detail Page
> Breadcrumb navigation, product gallery, stock indicator, and CTA buttons

![Product Detail](docs/screenshots/detail.png)

### Shop by Mood
> Interactive mood cards with grayscale-to-color hover transitions

![Shop by Mood](docs/screenshots/mood.png)

> **Note:** To add screenshots, create a `docs/screenshots/` directory and place your captured images there.

---

## 🛠️ Tech Stack

### Backend
| Technology | Version | Purpose |
|-----------|---------|---------|
| [Python](https://python.org) | 3.9+ | Runtime |
| [FastAPI](https://fastapi.tiangolo.com) | 0.115 | REST API framework |
| [Pydantic](https://docs.pydantic.dev) | 2.9 | Data validation & schemas |
| [Uvicorn](https://www.uvicorn.org) | 0.30 | ASGI server |

### Frontend
| Technology | Version | Purpose |
|-----------|---------|---------|
| [SvelteKit](https://svelte.dev) | 5.x | Frontend framework (Svelte 5 Runes mode) |
| [Tailwind CSS](https://tailwindcss.com) | 4.x | Utility-first CSS with `@theme` tokens |
| [Vite](https://vitejs.dev) | 8.x | Build tool & dev server |

### Infrastructure
| Technology | Purpose |
|-----------|---------|
| [Docker](https://docker.com) | Containerization |
| [Docker Compose](https://docs.docker.com/compose/) | Multi-service orchestration |

---

## 🏛️ Architecture

```
┌──────────────────┐         ┌──────────────────┐
│                  │   HTTP   │                  │
│   SvelteKit      │◄───────►│   FastAPI         │
│   Frontend       │  :5173  │   Backend         │
│   (Svelte 5 +    │         │   (Python +       │
│    Tailwind v4)  │         │    Pydantic)      │
│                  │         │                  │
│   Port: 5173     │         │   Port: 8000      │
└──────────────────┘         └──────┬───────────┘
                                    │
                             ┌──────▼───────────┐
                             │  Mock Database    │
                             │  (In-Memory)      │
                             │  12 Products      │
                             └──────────────────┘
```

**Data Flow:**
1. User visits the SvelteKit frontend
2. Components call `$lib/api.js` to fetch data
3. API client sends HTTP requests to FastAPI backend
4. FastAPI validates requests with Pydantic and returns JSON
5. Svelte reactively renders the UI with the API data

---

## 📁 Project Structure

```
gemandthreads/
│
├── 📂 backend/                      # FastAPI REST API
│   ├── 📂 app/
│   │   ├── __init__.py
│   │   ├── main.py                  # App entry point, CORS middleware
│   │   ├── models.py                # Pydantic schemas (Product, Category)
│   │   ├── database.py              # Mock in-memory database (12 products)
│   │   └── 📂 routers/
│   │       ├── __init__.py
│   │       └── products.py          # Product & Category endpoints
│   ├── requirements.txt             # Python dependencies
│   └── Dockerfile                   # Python 3.11-slim container
│
├── 📂 frontend/                     # SvelteKit + Tailwind CSS v4
│   ├── 📂 src/
│   │   ├── app.html                 # HTML template (fonts, meta)
│   │   ├── 📂 lib/
│   │   │   ├── api.js               # API client (fetchProducts, etc.)
│   │   │   └── 📂 components/       # Reusable Svelte components
│   │   │       ├── Navbar.svelte    # Glassmorphism pill navbar
│   │   │       ├── Hero.svelte      # "The Soul of the Hand" hero
│   │   │       ├── ProductCard.svelte # Hover-lift product card
│   │   │       ├── ShopByMood.svelte  # Calm/Energetic/Romantic
│   │   │       ├── ShopByOccasion.svelte # Wedding/Casual/Gifting
│   │   │       ├── InstagramFeed.svelte  # Community gallery
│   │   │       ├── Footer.svelte    # 3-column footer
│   │   │       └── BottomNav.svelte # Mobile bottom navigation
│   │   └── 📂 routes/
│   │       ├── layout.css           # Tailwind + design tokens
│   │       ├── +layout.svelte       # App shell (Navbar + Footer)
│   │       ├── +page.svelte         # Landing page
│   │       └── 📂 products/[id]/
│   │           └── +page.svelte     # Product detail page
│   ├── package.json
│   ├── svelte.config.js
│   ├── vite.config.js
│   └── Dockerfile                   # Node 20 Alpine container
│
├── 📄 docker-compose.yml            # Backend + Frontend services
├── 📄 README.md                     # You are here!
└── 📄 code*.html                    # Original HTML mockup references
```

---

## 🚀 Getting Started

### Prerequisites

- **Python** 3.9 or higher
- **Node.js** 20 or higher
- **npm** 10 or higher
- (Optional) **Docker** & **Docker Compose**

### Option 1: Docker Compose (Recommended)

The fastest way to run the entire app:

```bash
# Clone and start
git clone https://github.com/your-username/gemandthreads.git
cd gemandthreads

# Start both services
docker-compose up --build
```

| Service | URL |
|---------|-----|
| 🖥️ Frontend | http://localhost:5173 |
| ⚡ Backend API | http://localhost:8000 |
| 📖 Swagger Docs | http://localhost:8000/docs |
| 📘 ReDoc | http://localhost:8000/redoc |

### Option 2: Manual Setup

**1. Start the Backend**

```bash
cd backend

# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate    # macOS/Linux
# venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn app.main:app --reload --port 8000
```

The API will be available at `http://localhost:8000`.

**2. Start the Frontend**

```bash
cd frontend

# Install dependencies
npm install

# Run the dev server
npm run dev
```

The app will be available at `http://localhost:5173`.

---

## 📡 API Documentation

### Base URL

```
http://localhost:8000/api
```

### Endpoints

#### `GET /api/health`
Health check endpoint.

**Response:**
```json
{
  "status": "ok",
  "service": "Gem & Threads API"
}
```

---

#### `GET /api/products`
Returns all products. Supports optional category filtering.

**Query Parameters:**

| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `category` | string | No | Filter by `jewelry` or `crochet` |

**Example Request:**
```bash
# All products
curl http://localhost:8000/api/products

# Filter by category
curl http://localhost:8000/api/products?category=jewelry
```

**Response:**
```json
{
  "products": [
    {
      "id": 1,
      "name": "Aura Crystal Collection",
      "description": "Cleansed with sage, charged with intention...",
      "price": 124.00,
      "stock": 12,
      "category": "jewelry",
      "image_url": "https://...",
      "mood": "Calm",
      "materials": "Assorted Crystals, Sterling Silver Chain"
    }
  ],
  "total": 12
}
```

---

#### `GET /api/products/{id}`
Returns a single product by its ID.

**Path Parameters:**

| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | integer | Yes | Product ID |

**Example Request:**
```bash
curl http://localhost:8000/api/products/1
```

**Response:** Single `Product` object (same schema as above).

**Error Response (404):**
```json
{
  "detail": "Product with id 99 not found"
}
```

---

#### `GET /api/categories`
Returns all available categories.

**Example Request:**
```bash
curl http://localhost:8000/api/categories
```

**Response:**
```json
{
  "categories": [
    { "value": "jewelry", "label": "Jewelry" },
    { "value": "crochet", "label": "Crochet" }
  ]
}
```

---

### Data Schemas

#### Product

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | integer | ✅ | Unique identifier |
| `name` | string | ✅ | Product name |
| `description` | string | ✅ | Product description |
| `price` | float | ✅ | Price in USD (must be > 0) |
| `stock` | integer | ✅ | Available stock (must be ≥ 0) |
| `category` | enum | ✅ | `"jewelry"` or `"crochet"` |
| `image_url` | string | ✅ | URL of product image |
| `mood` | string | ❌ | Mood tag (Calm, Energetic, Romantic) |
| `materials` | string | ❌ | Materials used |

---

## 🎨 Design System

### Color Palette (Material Design 3)

The design system is based on a warm, feminine Material Design 3 palette:

| Token | Hex | Usage |
|-------|-----|-------|
| `primary` | `#80534c` | Main brand color (warm terracotta) |
| `primary-container` | `#e2a9a1` | Lighter variant, buttons, accents |
| `primary-fixed-dim` | `#f3b8b0` | Soft pink, underlines, badges |
| `surface` | `#fdf9f6` | Page background (warm white) |
| `on-surface` | `#1c1b1a` | Primary text color |
| `on-surface-variant` | `#514442` | Secondary text color |
| `secondary` | `#526442` | Accent green |
| `secondary-container` | `#d2e6bc` | Light green backgrounds |
| `outline-variant` | `#d5c2bf` | Borders and dividers |

### Typography

| Family | Font | Usage |
|--------|------|-------|
| `font-headline` | Noto Serif | Headings, prices, mood labels |
| `font-body` | Plus Jakarta Sans | Body text, descriptions |
| `font-label` | Plus Jakarta Sans | Buttons, tags, navigation |

### Iconography

Using [Material Symbols Outlined](https://fonts.google.com/icons) with variable font settings:
```css
font-variation-settings: 'FILL' 0, 'wght' 300, 'GRAD' 0, 'opsz' 24;
```

---

## 🧩 Components

### `<Navbar />`
Floating pill-shaped navigation bar with glassmorphism effect. Desktop shows full text links; mobile shows a hamburger menu overlay.

### `<Hero />`
Full-width hero banner with 12-column grid layout (5 text + 7 image on desktop). Includes "Shop the Collection" CTA with gradient hover effect.

### `<ProductCard product={...} />`
Product card with:
- `rounded-2xl` corners
- Soft pink shadow (`custom-shadow`)
- Hover lift effect (`scale-[1.02]` + `-translate-y-1`)
- Favorite button overlay on hover
- Mood badge on hover

### `<ShopByMood />`
Three pill-shaped image cards with `grayscale → color` hover transition and floating label reveal.

### `<ShopByOccasion />`
Asymmetric two-column layout with numbered list items (01, 02, 03) and chevron hover reveal.

### `<InstagramFeed />`
Responsive 2/3/6 column image grid with scale-110 zoom on hover.

### `<Footer />`
Three-column link layout (About, Support, Connect) with underline hover effects.

### `<BottomNav />`
Mobile-only (`md:hidden`) bottom navigation with glassmorphism and active state gradient indicator.

---

## ⚙️ Environment Variables

### Frontend

| Variable | Default | Description |
|----------|---------|-------------|
| `VITE_API_URL` | `http://localhost:8000` | Backend API base URL |

Create a `.env` file in the `frontend/` directory:

```env
VITE_API_URL=http://localhost:8000
```

---

## 🐳 Docker

### Docker Compose Services

| Service | Image | Port | Description |
|---------|-------|------|-------------|
| `backend` | Python 3.11-slim | 8000 | FastAPI with hot-reload |
| `frontend` | Node 20 Alpine | 5173 | SvelteKit dev server |

### Commands

```bash
# Start all services
docker-compose up --build

# Start in background
docker-compose up -d --build

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Rebuild specific service
docker-compose up --build backend
```

### Volume Mounts

Both services mount source code directories for hot-reload during development:

| Service | Host | Container |
|---------|------|-----------|
| Backend | `./backend` | `/app` |
| Frontend | `./frontend` | `/app` |

---

## 🗺️ Roadmap

- [ ] Add real database (PostgreSQL / SQLite)
- [ ] User authentication & accounts
- [ ] Shopping cart functionality
- [ ] Order management
- [ ] Search functionality
- [ ] Dark mode toggle
- [ ] Product image gallery (multiple images)
- [ ] Admin dashboard
- [ ] Payment integration
- [ ] Deployment (Vercel + Railway/Fly.io)

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

<p align="center">
  <em>Handcrafted with intention 💎🧶</em>
</p>
