from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class Category(str, Enum):
    """Product categories for Gem & Threads boutique."""
    jewelry = "jewelry"
    crochet = "crochet"


class Product(BaseModel):
    """Schema for a single product."""
    id: int
    name: str
    description: str
    price: float = Field(..., gt=0, description="Product price in USD")
    stock: int = Field(..., ge=0, description="Available stock quantity")
    category: Category
    image_url: str
    mood: Optional[str] = Field(None, description="Mood tag (e.g., Calm, Energetic, Romantic)")
    materials: Optional[str] = Field(None, description="Materials used in the product")

    model_config = {"json_schema_extra": {
        "example": {
            "id": 1,
            "name": "Aura Crystal Collection",
            "description": "Cleansed with sage, charged with intention.",
            "price": 124.00,
            "stock": 12,
            "category": "jewelry",
            "image_url": "https://example.com/image.jpg",
            "mood": "Calm",
            "materials": "Rose Quartz, 14k Gold"
        }
    }}


class ProductList(BaseModel):
    """Response schema for a list of products."""
    products: list[Product]
    total: int
