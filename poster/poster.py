from PIL import Image, ImageDraw, ImageFont
import copy


class Poster:
    # class module in package target root dir for file i/o by default
    template = Image.open("./input/stage2.jpg")
    canva = Image.new(
        "RGB",
        template.size,
        "white"
    )
    canva.paste(template, (0, 0))

    fonts = {
        "name_font": ImageFont.truetype("./fonts/Cutest Things.ttf", 50),
        "age_font": ImageFont.truetype("./fonts/Impact.ttf", 50),
        "id_font": ImageFont.truetype("./fonts/Impact.ttf", 100),
        "link_font": ImageFont.truetype("./fonts/user_link.ttf", 40),
        "to_vote_font": ImageFont.truetype("./fonts/user_link.ttf", 28)
    }

    def __init__(self, user: dict):
        self.user = user
        self.canva = copy.deepcopy(Poster.canva)

    def add_profile_picture_to_image(self):
        user_id, file_ext = self.user["id"], self.user["image_format"]
        profile_picture = None

        try:
            profile_picture = Image.open(f"./pictures/{user_id}.{file_ext}")
        except FileNotFoundError:
            print(f"Problem with picture: {user_id}{file_ext}")
            return

        width, height = profile_picture.size
        cropped_image = profile_picture.crop((0, 0, width, width))

        mask = Image.new("L", (width, width), 0)
        mask_draw = ImageDraw.Draw(mask)
        mask_draw.ellipse((0, 0, width, width), fill=255)

        cropped_image.putalpha(mask)
        image = cropped_image.resize((500, 500))
        self.canva.paste(image, (500, 500), image)

    def write_user_details_to_image(self):
        d1 = ImageDraw.Draw(self.canva)
        d1.text(
            (750, 1100),
            self.format_name(self.user["name"]),
            fill="#000",
            font=self.fonts["name_font"],
            anchor="mm"
        )

    @staticmethod
    def format_name(self, name: str):
        name = name.strip()
        if len(name) > 25 and name.count(" ") > 1:
            split_names = name.split(" ")
            return f"{split_names[0]} {split_names[-1]}".title()

        return name.title()

    def save_file(self, dir_path="./output/"):
        user_id = self.user["id"]
        self.canva.save(f"{dir_path}{user_id}.jpeg")
        # print(f"{user_id}.jpeg saved")
