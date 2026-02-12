from pydantic import BaseModel

# Request model for creating/updating item
class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True
