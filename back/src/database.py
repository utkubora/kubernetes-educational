import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load .env in development (no effect in prod if not present)
load_dotenv()

class MongoDBClient:
    def __init__(self):
        self.username = os.getenv("MONGO_USERNAME")
        self.password = os.getenv("MONGO_PASSWORD")
        self.host = os.getenv("MONGO_HOST", "localhost")
        self.port = int(os.getenv("MONGO_PORT", 27017))
        self.db_name = os.getenv("MONGO_DB")

        if not all([self.username, self.password, self.db_name]):
            raise ValueError("Missing required MongoDB environment variables")

        # Construct connection string securely
        self.uri = f"mongodb://{self.username}:{self.password}@{self.host}:{self.port}"

        self.client = MongoClient(
            self.uri,
            serverSelectionTimeoutMS=5000,  # Fail fast
            maxPoolSize=10,                # Connection pooling
        )

        self.db = self.client[self.db_name]

    def get_collection(self, name: str):
        return self.db[name]
    
def mongo_insertOne(collection,user):
    #user = {
    #    "name": "Utku",
    #    "role": "Engineer",
    #    "skills": ["Python", "MongoDB", "DevOps"]
    #}

    result = collection.insert_one(user)

    print(f"Inserted ID: {result.inserted_id}")

def mongo_findAll(collection):
    users = collection.find()
    return users