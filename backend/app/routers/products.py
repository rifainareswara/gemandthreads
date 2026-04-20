from fastapi import APIRouter, HTTPException, Query
from typing import Optional

from app.models import Product, ProductList, Category
from app.database import get_all_products, get_product_by_id, get_products_by_category

router = APIRouter(prefix="/api", tags=["products"])


@router.get("/products", response_model=ProductList)
async def list_products(category: Optional[str] = Query(None, description="Filter by category: 'jewelry' or 'crochet'")):
    """
    Fetch all products, optionally filtered by category.
    
    - **category**: Filter by 'jewelry' or 'crochet' (optional)
    """
    if category:
        # Validate category value
        if category not in [c.value for c in Category]:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid category '{category}'. Must be one of: {[c.value for c in Category]}"
            )
        products = get_products_by_category(category)
    else:
        products = get_all_products()

    return ProductList(products=products, total=len(products))


@router.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: int):
    """
    Fetch a single product by its ID.
    
    - **product_id**: The unique identifier of the product
    """
    product = get_product_by_id(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail=f"Product with id {product_id} not found")
    return product


@router.get("/categories")
async def list_categories():
    """
    List all available product categories.
    """
    return {
        "categories": [
            {"value": c.value, "label": c.value.capitalize()}
            for c in Category
        ]
    }
