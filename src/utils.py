# File holds some utility functions that may be called inside of the main 


from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

# Path to access images
IMAGE_PATH='../images/'

class utils:
    def create_image_for(text, name):
        img = Image.open(IMAGE_PATH+'default.jpeg')
        draw = ImageDraw.Draw(img)

        font = ImageFont.truetype('arial', 24)
        draw.text((0, 0),text,(255,255,255),font=font)
        img.save(name+'.jpeg')
