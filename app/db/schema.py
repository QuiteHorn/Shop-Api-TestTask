from pydantic import BaseModel


# Category

class CategoryCreate(BaseModel):
    category_name: str
    description: str

class CategoryUpdate(BaseModel):
    description: str

# --------------------------

# Seller

class SellerCreate(BaseModel):
    seller_name: str

# --------------------------

# Item

class ItemCreate(BaseModel):
    item_name: str
    color: str
    in_stock: bool
    category_id: int
    seller_id: int

class ItemUpdate(BaseModel):
    item_name: str
    color: str
    in_stock: bool

# --------------------------
