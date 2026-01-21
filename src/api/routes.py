from fastapi import APIRouter
import sqlite3
from neo4j import GraphDatabase
from pymilvus import connections, Collection

router = APIRouter()

@router.get("/recommendations/{user_id}")
def recommend(user_id: str):
    # Milvus: find similar users
    connections.connect("default", host="localhost", port="19530")
    collection = Collection("conversation_embeddings")
    results = collection.query(expr=f"user_id == '{user_id}'", output_fields=["user_id", "message_id"])

    similar_users = [r["user_id"] for r in results][:5]

    # Neo4j: fetch campaigns linked to similar users
    driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "test"))
    campaigns = []
    with driver.session() as session:
        for u in similar_users:
            res = session.run("MATCH (u:User {id:$user})-[:ENGAGED]->(c:Campaign) RETURN c.id", user=u)
            campaigns.extend([r["c.id"] for r in res])

    # SQLite: rank campaigns by frequency
    conn = sqlite3.connect("db/analytics.db")
    cur = conn.cursor()
    ranked = {}
    for c in campaigns:
        cur.execute("SELECT COUNT(*) FROM interactions WHERE campaign_id=?", (c,))
        ranked[c] = cur.fetchone()[0]
    conn.close()

    ranked_sorted = sorted(ranked.items(), key=lambda x: x[1], reverse=True)

    return {"user_id": user_id, "recommendations": ranked_sorted}
