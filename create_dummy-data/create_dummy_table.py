"""Create Dummy Table.

    ライブラリ『Faker」を使用したダミーテーブルを作成するサンプルコード。
    LINE ID,Agent,Userのテーブルのサンプルを作成。

"""

from faker import Faker
import random
import csv
from typing import List, Dict, TextIO, cast
from datetime import datetime, timedelta

fake = Faker()
fake_jp = Faker('ja_JP')  # 日本語で作成したい場合
Faker.seed(0)

num_messages = 100000


def create_line_id_table():
    num_users = 1000
    line_id_table = []
    for i in range(num_users):
        line_id = random.randint(1, 1000)
        create_time = datetime.now() - timedelta(days=random.randint(0, 365),
                                                 seconds=random.randint(0,
                                                                        86400))
        line_id_table.append({
            "line_id": line_id,
            "create_at": create_time.isoformat()
        })

    save_to_csv(line_id_table, "result/line_id_table.csv")

    return line_id_table


def create_user_table(line_id_table):
    user_table = []
    for i in line_id_table:
        user_id = random.randint(1001, 2000)
        store_name = restaurant_name()  # Fakerになくても自作できる
        line_id = i["line_id"]
        agent_id = random.randint(2001, 3000)
        icon_url = f"https://buket_name.s3.ap-northeast-1.amazonaws.com/{fake.file_name(category='image')}"
        stage = random.choice(["NEW", "EXISTING", "PROSPECT"])
        create_at = i["create_at"]
        update_at = datetime.now() - timedelta(days=random.randint(0, 365),
                                               seconds=random.randint(0,
                                                                      86400))

        user_table.append({
            "user_id": user_id,
            "store_name": store_name,
            "line_id": line_id,
            "agent_id": agent_id,
            "icon_url": icon_url,
            "stage": stage,
            "create_at": create_at,
            "update_at": update_at.isoformat()
        })

    save_to_csv(user_table, "result/user_table.csv")

    return user_table


def restaurant_name():
    types = ["Cafe", "Bistro", "Bar", "Grill", "Kitchen", "Diner", "Eatery",
             "Bakery"]
    adj = ["Cozy", "Sunny", "Golden", "Spicy", "Charming", "Delicious",
           "Rustic"]
    themes = ["Garden", "Corner", "Table", "House", "Plate", "Spot", "Hut",
              "Lounge"]
    name = f"{random.choice(adj)}{random.choice(themes)}{random.choice(types)}"
    return name


def agent_table(user_table):
    agent_id_list = []
    for j in user_table:
        agent_id_list.append(j["agent_id"])

    agent_id_table = []
    for i in range(100):
        agent_id = random.choice(agent_id_list)
        agent_name = fake_jp.name()
        agent_img = f"https://buket_name.s3.ap-northeast-1.amazonaws.com/{fake.file_name(category='image')}"
        agent_group = random.choice(["Group1", "Group2", "Group3", "Group4"])
        create_at = datetime.now() - timedelta(days=random.randint(0, 365),
                                               seconds=random.randint(0,
                                                                      86400))
        update_at = datetime.now() - timedelta(days=random.randint(0, 365),
                                               seconds=random.randint(0,
                                                                      86400))

        agent_id_table.append({
            "agent_id": agent_id,
            "agent_name": agent_name,
            "agent_img": agent_img,
            "agent_group": agent_group,
            "create_at": create_at.isoformat(),
            "update_at": update_at.isoformat()
        })

    save_to_csv(agent_id_table, "result/agent_table.csv")

    return agent_id_table


def save_to_csv(data: List[Dict[str, str]], filename: str) -> None:
    with open(filename, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())  # type: ignore
        writer.writeheader()
        writer.writerows(data)


def main():
    line_id_table = create_line_id_table()
    user_table = create_user_table(line_id_table)
    agent_table(user_table)


if __name__ == "__main__":
    main()
