from sentence_transformers import SentenceTransformer
import json

def generate_embeddings(input_file="data/sample_conversations.json"):
    model = SentenceTransformer("all-MiniLM-L6-v2")

    with open(input_file, "r") as f:
        conversations = json.load(f)

    for conv in conversations:
        embedding = model.encode(conv["message"]).tolist()
        conv["embedding"] = embedding

    with open("data/conversations_with_embeddings.json", "w") as f:
        json.dump(conversations, f, indent=2)

if __name__ == "__main__":
    generate_embeddings()
    print("✅ Embeddings generated and stored.")
