from fastapi import FastAPI, HTTPException
from models import Item
from schemas import ItemResponse
from database import items_db

app = FastAPI()

# Auto-increment ID counter
item_id_counter = 1


# Home route
@app.get("/")
def home():
    return {"message": "Welcome to Safi's Store API 🚀"}


# Create Item (POST)
@app.post("/items/", response_model=ItemResponse)
def create_item(item: Item):
    global item_id_counter
    items_db[item_id_counter] = item.dict()
    response = {
        "id": item_id_counter,
        "name": item.name,
        "price": item.price,
        "in_stock": item.in_stock,
        "message": "Item created successfully ✅"
    }
    item_id_counter += 1
    return response


# Read Item (GET)
@app.get("/items/{item_id}", response_model=ItemResponse)
def get_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found ❌")

    item = items_db[item_id]
    return {
        "id": item_id,
        "name": item["name"],
        "price": item["price"],
        "in_stock": item["in_stock"],
        "message": "Item fetched successfully ✅"
    }


# Update Item (PUT)
@app.put("/items/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item: Item):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found ❌")

    items_db[item_id] = item.dict()
    return {
        "id": item_id,
        "name": item.name,
        "price": item.price,
        "in_stock": item.in_stock,
        "message": "Item updated successfully 🔄"
    }


# Delete Item (DELETE)
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found ❌")

    del items_db[item_id]
    return {"message": f"Item {item_id} deleted successfully 🗑️"}

