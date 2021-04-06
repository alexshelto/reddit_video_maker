# File holds some utility functions that may be called inside of the main 

import os.path #used to create image file path

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

# Path to access images
IMAGE_PATH='../images/'
FONT_PATH ='../fonts/'

class utils:

    @staticmethod
    def split_string(text, n):
        '''splits a string into indexes of a list
        each index holds n words'''
        words = text.split() #splits words into list: eg: 'hello world' -> ['hello', 'world']
        lines = []
        line = ''
        added = False

        wc = 0 # Word count
        for word in words:
            added = False
            line += word + ' '
            wc += 1
            if (wc % n == 0):
                lines.append(line)
                line = ''
                added = True

        if (added is False):
            lines.append(line)

        return lines



    def create_image_for(text, name):
        # Creating the file path to save the image. 
        text = text.decode("utf-8")
        complete_file = os.path.join(IMAGE_PATH, name+'.jpeg')
        # Creating the file path to open font file
        font_file = os.path.join(FONT_PATH, 'AppleGothic.ttf')

        # Opening default image from path
        img = Image.open(IMAGE_PATH+'default.jpeg')
        # Allowing us to draw to it
        draw = ImageDraw.Draw(img)
        # Creating font and text size
        font = ImageFont.truetype(font_file, 50)
        # Writing post tile || comment to pic
        #draw.text((0, 0),text,font=font,fill=(255,255,255))
        
        # Need to loop through the words, and put them on the file line by line
        # If i write all text at once itl overflow off the picture in 1 line
        # Splitting each line of text into 10 words
        y = 0 # starting y index
        for line in utils.split_string(text, 10):
            print(f'line: {line}\n')
            draw.text((0, y),line,font=font,fill=(255,255,255))
            y += 50 # adding 50 pixel buffer to next line

        # Saving the picture
        img.save(complete_file)

