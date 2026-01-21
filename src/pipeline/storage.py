import json
from pymongo import MongoClient
from pymilvus import connections, Collection, FieldSchema, CollectionSchema, DataType
from neo4j import GraphDatabase
import sqlite3

def store_data(input_file="data/conversations_with_embeddings.json"):
    with open(input_file, "r") as f:
        conversations = json.load(f)

    # MongoDB
    mongo_client = MongoClient("mongodb://localhost:27017/")
    db = mongo_client["marketing"]
    mongo_collection = db["conversations"]
    mongo_collection.insert_many(conversations)

    # Milvus
    connections.connect("default", host="localhost", port="19530")
    fields = [
        FieldSchema(name="user_id", dtype=DataType.VARCHAR, max_length=20),
        FieldSchema(name="message_id", dtype=DataType.VARCHAR, max_length=20),
        FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=384)
    ]
    schema = CollectionSchema(fields, description="Conversation embeddings")
    collection = Collection("conversation_embeddings", schema)
    for conv in conversations:
        collection.insert([[conv["user_id"]], [conv["message_id"]], [conv["embedding"]]])

    # Neo4j
    driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "test"))
    with driver.session() as session:
        for conv in conversations:
            session.run(
                "MERGE (u:User {id:$user}) "
                "MERGE (c:Campaign {id:$campaign}) "
                "MERGE (u)-[:ENGAGED]->(c)",
                user=conv["user_id"], campaign=conv["campaign_id"]
            )

    # SQLite
    conn = sqlite3.connect("db/analytics.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS interactions (user_id TEXT, campaign_id TEXT, count INT)")
    for conv in conversations:
        cur.execute("INSERT INTO interactions VALUES (?, ?, ?)", (conv["user_id"], conv["campaign_id"], 1))
    conn.commit()
    conn.close()

    print("✅ Data stored in MongoDB, Milvus, Neo4j, and SQLite.")

if __name__ == "__main__":
    store_data()
