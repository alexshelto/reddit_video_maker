# ImageCreator.py
# Called after the Reddit Post content has been scraped 
# 
# Creates an image of the text for all posts, eg: title and replies
#
#


# File holds some utility functions that may be called inside of the main

import os.path  # used to create image file path

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# Path to access images
IMAGE_PATH = '../images/'
FONT_PATH = '../fonts/'


class ImageCreator:
    def create_image_for(text, author, name):
        '''takes a string of text, an author, and a name that the file should be
        writes the text to the background of a default image in ../images/
        saves the image as a new image to name.jpeg'''
        # Creating the file path to save the image. 

        # text = text.decode("utf-8")

        complete_file = os.path.join(IMAGE_PATH, name + '.jpeg')
        # Creating the file path to open font file
        font_file = os.path.join(FONT_PATH, 'AppleGothic.ttf')

        # Opening default image from path
        img = Image.open(IMAGE_PATH + 'default.jpeg')
        # Allowing us to draw to it
        draw = ImageDraw.Draw(img)
        # Creating font and text size
        font = ImageFont.truetype(font_file, 50)

        # Creating author font: slightly larger than text size
        author_font = ImageFont.truetype(font_file, 55)
        # Writing author name to file
        draw.text((20, 50), f'u/{author}', font=author_font, fill=(225, 0, 0))

        # Need to loop through the words, and put them on the file line by line
        # If i write all text at once itl overflow off the picture in 1 line
        # Splitting each line of text into 10 words
        image_height = 1080
        image_width = 1920
        y = 150  # starting y index

        for line in ImageCreator.split_string(text, 10):
            text_dimensions = ImageCreator.get_text_dimensions(line, font)
            x = (image_width - text_dimensions[0]) / 2

            draw.text((x, y), line, font=font, fill=(255, 255, 255))
            y += 50  # adding 50 pixel buffer to next line

        # Saving the picture
        img.save(complete_file)

    def get_text_dimensions(text_string, font):
        """takes a string of text that I am going to put onto an image
        tells me how many pixels tall & wide the text will be and returns.
        this helps decide where to place the text on the screen"""
        # https://stackoverflow.com/a/46220683/9263761
        ascent, descent = font.getmetrics()
        text_width = font.getmask(text_string).getbbox()[2]
        text_height = font.getmask(text_string).getbbox()[3] + descent
        return text_width, text_height

    def split_string(text, n):
        """splits a string into indexes of a list
        each index holds n words

        ex: split_string('hello world hello world', 2)
        => ['hello world', 'hello world']"""
        words = text.split()  # splits words into list: eg: 'hello world' -> ['hello', 'world']
        lines = []
        line = ''
        added = False

        wc = 0  # Word count
        for word in words:
            added = False
            line += word + ' '
            wc += 1
            if wc % n == 0:
                lines.append(line)
                line = ''
                added = True

        if added is False:
            lines.append(line)

        return lines
