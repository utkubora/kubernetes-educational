from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from database import MongoDBClient,mongo_insertOne,mongo_findAll

# Create the FastAPI application instance
app = FastAPI(
    title="Simple FastAPI API",
    description="A minimal example API with GET and POST endpoints",
    version="1.0.0"
)

mongo_client = MongoDBClient()
user_collection = mongo_client.get_collection("User")

# Request/response model
class User(BaseModel):
    name: str
    role: str
    skills: List[str] = []


@app.get("/")
def read_root():
    """
    Health / welcome endpoint
    """
    return {"message": "FastAPI is running"}


@app.get("/items", response_model=List[User])
def get_items():
    """
    Return all items
    """

    items_db = mongo_findAll(user_collection)

    return items_db


@app.get("/items/{item_id}", response_model=User)
def get_item(item_id: int):
    """
    Return one item by ID
    """
    #for item in items_db:
    #    if item.id == item_id:
    #        return item
        
    items_db = mongo_findAll(user_collection)

    raise HTTPException(status_code=404, detail="Item not found")


@app.get("/add", response_model=User, status_code=201)
def create_item():
    """
    Create a new item
    """
    # Check if item with same ID already exists
    #for existing_item in items_db:
    #    if existing_item.id == item.id:
    #        raise HTTPException(status_code=400, detail="Item with this ID already exists")
    item = User(name="Utku",role="Engineer",skills=["Python", "MongoDB", "DevOps"])
    mongo_insertOne(user_collection,item.model_dump(mode="python"))
    return item