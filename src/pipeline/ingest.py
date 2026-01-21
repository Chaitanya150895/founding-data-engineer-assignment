import json
import datetime
import random

def generate_sample_data(num_records=20):
    users = ["u1", "u2", "u3", "u4", "u5"]
    campaigns = ["c1", "c2", "c3"]

    data = []
    for i in range(num_records):
        record = {
            "user_id": random.choice(users),
            "message_id": f"m{i}",
            "campaign_id": random.choice(campaigns),
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "message": f"Sample message {i}"
        }
        data.append(record)

    with open("data/sample_conversations.json", "w") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    generate_sample_data()
    print("✅ Sample conversation data generated.")
