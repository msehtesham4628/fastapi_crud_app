from pydantic import BaseModel

# Response model
class ItemResponse(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool
    message: str

