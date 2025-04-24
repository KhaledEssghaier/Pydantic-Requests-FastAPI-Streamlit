from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Modèle de données
class Item(BaseModel):
    text: str
    is_done: bool = False

# Liste pour stocker les items (avec un exemple)
items: list[Item] = [Item(text="Hello world")]

# Route principale
@app.get("/")
def root():
    return {"Hello": "World"}

# Créer un nouvel item
@app.post("/items", response_model=Item)
def create_item(item: Item):
    items.append(item)
    return item

# Récupérer un item par son ID
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    if 0 <= item_id < len(items):
        return items[item_id]
    raise HTTPException(status_code=404, detail=f"Item {item_id} not found")

# Lister plusieurs items
@app.get("/items", response_model=list[Item])
def list_items(limit: int = 10):
    return items[:limit]
