import csv
from os import path
import requests


LINK = "https://kiddiescrown.com/"
FILE = "input/contestants.csv"


def main():
    users = load_users()
    for user in users:
        file_link, user_id = user["picture"], user["id"]
        download_img(file_link, user_id)


def load_users():
    users = []
    with open(FILE, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            user = dict({
                "id": row["id"],
                "picture": row["picture"]
            })
            users.append(user)

    return users


def download_img(file_link: str, user_id: str):
    file_ext = file_link.split(".")[-1]

    if path.exists(f"./pictures/{user_id}.{file_ext}"):
        print(f"{user_id}.{file_ext} already exists")
        return

    try:
        response = requests.get(LINK+file_link)
        file = open(f"./pictures/{user_id}.{file_ext}", "wb")
        file.write(response.content)
        file.close()
        print(f"'{user_id}' picture saved successfully")
    except requests.RequestException as e:
        print(f"Request failed: {e}")
    except IOError as e:
        print(f"File operation failed: {e}")


main()
