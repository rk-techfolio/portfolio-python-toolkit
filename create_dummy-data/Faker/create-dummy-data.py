from faker import Faker
import random
import csv
from datetime import datetime, timedelta

fake = Faker()
Faker.seed(0)

num_users = 1000
num_messages = 10000
user_ids = [f"user_{i}" for i in range(num_users)]

dummy_data = []
for i in range(num_messages):
    user_id = random.choice(user_ids)
    user_name = fake.user_name()
    user_phone = fake.phone_number()
    user_comp = fake.company()
    message_id = f"msg_{i}"
    message_content = fake.sentence(nb_words=10)
    timestamp = datetime.now() - timedelta(days=random.randint(0, 365), seconds=random.randint(0, 86400))
    chat_room_id = f"room_{random.randint(1, 50)}"

    dummy_data.append({
        "user_id": user_id,
        "user_name": user_name,
        "user_phone": user_phone,
        "user_company": user_comp,
        "message_id": message_id,
        "message_content": message_content,
        "timestamp": timestamp.isoformat(),
        "chat_room_id": chat_room_id
    })

with open("dummy_message.csv", "w", newline="") as csvfile:
    fieldnames = ["user_id", "user_name", "user_phone", "user_company", "message_id", "message_content", "timestamp", "chat_room_id"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(dummy_data)

