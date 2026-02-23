from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Items API - Starter")

class Item(BaseModel):
    id: Optional[int] = None
    name: str
    price: float

# simple in-memory store
_db = {}
_next_id = 1

@app.get("/items")
def list_items():
    return list(_db.values())

@app.get("/items/{item_id}")
def get_item(item_id: int):
    item = _db.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/items", status_code=201)
def create_item(item: Item):
    global _next_id
    item.id = _next_id
    _db[_next_id] = item.dict()
    _next_id += 1
    return _db[item.id]

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in _db:
        raise HTTPException(status_code=404, detail="Item not found")
    item.id = item_id
    _db[item_id] = item.dict()
    return _db[item_id]

@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in _db:
        raise HTTPException(status_code=404, detail="Item not found")
    del _db[item_id]
    return None
