from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random


class ImageGenerator:

    def __init__(self, data, width=600, height=600, background="white"):
        self.data = data
        self.img = Image.new("RGB", (width, height), background)
        self.draw = ImageDraw.Draw(self.img)

    def word_cloud_company_size_by_project(self):

        for i in self.data:
            text_content = i[0]
            text_style = "text_file/Sylfaen.ttf"

            # Normalized the text size
            if i[2] == 1:
                font = ImageFont.truetype(text_style, i[2] * 28)
            elif i[2] == 2:
                font = ImageFont.truetype(text_style, i[2] * 15)
            elif i[2] == 3:
                font = ImageFont.truetype(text_style, i[2] * 12)
            elif i[2] >= 5 or i[2] <= 7:
                font = ImageFont.truetype(text_style, i[2] * 7)
            else:
                font = ImageFont.truetype(text_style, i[2] * 7)

            self.draw.text((random.randint(0, 500), random.randint(0, 550)), text_content, i[1], font)

        self.img.save('images/company_name_by_project.png')
        print("\n - - - Image successfully created and saved! - - -")

    def word_cloud_project_by_budget(self):

        for row in self.data:
            # normalized the number, divide by 1000
            font_size = int(row[1] / 1000)
            text_content = row[0]
            text_style = "text_file/Sylfaen.ttf"

            if row[2] is None:
                row[2] = "#af7"

            if font_size == 0:
                font = ImageFont.truetype(text_style, font_size + 1 * 20)
            elif font_size == 1:
                font = ImageFont.truetype(text_style, font_size * 25)
            elif font_size == 2:
                font = ImageFont.truetype(text_style, font_size * 15)
            elif font_size == 3:
                font = ImageFont.truetype(text_style, font_size * 11)
            elif font_size == 4:
                font = ImageFont.truetype(text_style, font_size * 9)
            elif font_size <= 7:
                font = ImageFont.truetype(text_style, font_size * 6)
            elif font_size <= 9:
                font = ImageFont.truetype(text_style, font_size * 5)
            else:
                font = ImageFont.truetype(text_style, font_size * 8)

            self.draw.text((random.randint(0, 700), random.randint(0, 850)), text_content, row[2], font)

        self.img.save('images/project_name_by_budget.png')
        print("\n - - - Image successfully created and saved! - - -")

    def word_cloud_bigger_than_avg(self):

        for line in self.data:
            text_content = line[0]
            if float(line[2]) <= 6000:
                font = ImageFont.truetype("text_file/SEASRN__.ttf", 15)
            elif float(line[2]) <= 7000:
                font = ImageFont.truetype("text_file/Capture_it.ttf", 30)
            elif float(line[2]) <= 8000:
                font = ImageFont.truetype("text_file/FFF_Tusj.ttf", 45)
            else:
                font = ImageFont.truetype("text_file/Capture_it.ttf", 60)

            self.draw.text((random.randint(0, 600), random.randint(0, 850)), text_content, line[3], font)

        self.img.save('images/bigger_than_average.png')
        print("\n - - - Image successfully created and saved! - - -")

    def word_cloud_name_status_by_color(self):
        # overridden the self.img(!), in this case, we have to overridden the self.draw too
        self.img = Image.open("images/land_900_900.png")
        self.draw = ImageDraw.Draw(self.img)

        text_style = "text_file/Sylfaen.ttf"

        for line in self.data:
            text_content = line[0]

            if line[1] == 1:
                font = ImageFont.truetype(text_style, random.randint(28, 33))
            elif line[1] == 2:
                font = ImageFont.truetype(text_style, random.randint(33, 36))
            elif line[1] == 3:
                font = ImageFont.truetype(text_style, random.randint(40, 44))
            else:
                font = ImageFont.truetype(text_style, random.randint(45, 50))

            self.draw.text((random.randint(0, 700), random.randint(0, 850)), text_content, line[2], font)

        # save the image to the images directory
        self.img.save('images/name_status_by_color.png')
        print("\n - - - Image successfully created and saved! - - -")
