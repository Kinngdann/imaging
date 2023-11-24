from poster import Poster
import csv
from tqdm import tqdm


FILE = "input/contestants.csv"


def main():
    users = load_users()

    for user in tqdm(users):
        poster = Poster(user)
        poster.add_profile_picture_to_image()
        poster.write_user_details_to_image()
        poster.save_file()
        # exit()


def load_users():
    users = []
    with open(FILE, encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            user = {
                "id": row["id"],
                "name": row["name"],
                "age": row["age"],
                "image_format": row["picture"].split(".")[-1]
            }
            users.append(user)

    return users


if __name__ == "__main__":
    main()
