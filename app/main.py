from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.db.models import Item, Category, Seller
from app.db.schema import ItemCreate, ItemUpdate, CategoryCreate, CategoryUpdate, SellerCreate


app = FastAPI()

# CATEGORIES SECTION

@app.get("/categories")
def get_all_categories(db: Session = Depends(get_db)):
    return db.query(Category).all()

@app.get("/categories/{category_id}")
def get_category_by_id(category_id: int, db: Session = Depends(get_db)):
    category = db.query(Category).filter(Category.id == category_id).first()
    if category:
        return category
    raise HTTPException(status_code=404, detail="Category not found")

@app.post("/categories")
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = Item(category_name=category.category_name, description=category.description)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

@app.put("/categories/{category_id}")
def update_category_by_id(category_id: int, category: CategoryUpdate, db: Session = Depends(get_db)):
    db_category = db.query(Item).filter(Category.id == category_id).first()
    if not db_category:
        raise HTTPException(status_code=404, detail="Item not found")
    db_category.description = category.description
    db.commit()
    return {"message": "Category updated"}

@app.delete("/categories/{category_id}")
def delete_category_by_id(category_id: int, db: Session = Depends(get_db)):
    db_category = db.query(Category).filter(Category.id == category_id).first()
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")
    db.delete(db_category)
    db.commit()
    return {"message": "Category deleted"}

# --------------------------------------

# SELLER SECTION

@app.get("/sellers")
def get_all_sellers(db: Session = Depends(get_db)):
    return db.query(Seller).all()

@app.get("/sellers/{seller_id}")
def get_seller_by_id(seller_id: int, db: Session = Depends(get_db)):
    seller = db.query(Category).filter(Seller.id == seller_id).first()
    if seller:
        return seller
    raise HTTPException(status_code=404, detail="Category not found")

@app.post("/sellers")
def create_sellery(seller: SellerCreate, db: Session = Depends(get_db)):
    db_seller = Item(seller_name=seller.seller_name)
    db.add(db_seller)
    db.commit()
    db.refresh(db_seller)
    return db_seller

@app.delete("/sellers/{seller_id}")
def delete_seller_by_id(seller_id: int, db: Session = Depends(get_db)):
    db_seller = db.query(Seller).filter(Seller.id == seller_id).first()
    if not db_seller:
        raise HTTPException(status_code=404, detail="Seller not found")
    db.delete(db_seller)
    db.commit()
    return {"message": "Seller deleted"}

# --------------------------------------

# ITEMS SECTION


@app.get("/items")
def get_all_items(item_name: str | None = None, color: str | None = None, in_stock: bool | None = None, category_id: int | None = None, seller_id: int | None = None, db: Session = Depends(get_db)):
    query = db.query(Item)
    if item_name:
        query = query.filter(Item.item_name == item_name)
    if color:
        query = query.filter(Item.color == color)
    if in_stock:
        query = query.filter(Item.in_stock == in_stock)
    if category_id:
        query = query.filter(Item.category_id == category_id)
    if seller_id:
        query = query.filter(Item.seller_id == seller_id)
    return query.all()

@app.get("/items/{item_id}")
def get_item_by_id(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item:
        return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items")
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(item_name=item.item_name, color=item.color, in_stock=item.in_stock, category_id=item.category_id, seller_id=item.seller_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/items/{item_id}")
def update_item_by_id(item_id: int, item: ItemUpdate, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db_item.item_name = item.item_name
    db_item.color = item.color
    db_item.in_stock = item.in_stock
    db.commit()
    return {"message": "User updated successfully"}

@app.delete("/items/{item_id}")
def delete_item_by_id(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return {"message": "Item deleted"}

# --------------------------------------
