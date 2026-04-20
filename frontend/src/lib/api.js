/**
 * API client for Gem & Threads backend.
 */

const BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

/**
 * Fetch all products, optionally filtered by category.
 * @param {string} [category] - 'jewelry' or 'crochet'
 * @returns {Promise<{products: Array, total: number}>}
 */
export async function fetchProducts(category) {
  const url = new URL(`${BASE_URL}/api/products`);
  if (category) {
    url.searchParams.set('category', category);
  }
  const res = await fetch(url.toString());
  if (!res.ok) throw new Error(`Failed to fetch products: ${res.statusText}`);
  return res.json();
}

/**
 * Fetch a single product by ID.
 * @param {number} id
 * @returns {Promise<Object>}
 */
export async function fetchProduct(id) {
  const res = await fetch(`${BASE_URL}/api/products/${id}`);
  if (!res.ok) throw new Error(`Failed to fetch product ${id}: ${res.statusText}`);
  return res.json();
}

/**
 * Fetch available categories.
 * @returns {Promise<{categories: Array}>}
 */
export async function fetchCategories() {
  const res = await fetch(`${BASE_URL}/api/categories`);
  if (!res.ok) throw new Error(`Failed to fetch categories: ${res.statusText}`);
  return res.json();
}
