# This clas will hold the class that edits the images into video

import cv2 # this is the video editing library
import os  # used for some file grabbing
from PIL import Image # Image library

class VideoEditor:
    def __init__(self,num_images):
        self.num_images = num_images
        self.image_path = '../images/'
        self.audio_path = '../audio/'

    
    def create_movie(self):
        ''' Method will make a slide show movie out of the audio and images
        '''
        video_name = 'reddit_movie.mp4'

        # Creating a list of all the images we have
        images = [img for img in os.listdir(self.image_path)
              if img.endswith(".jpg") or
                 img.endswith(".jpeg") or
                 img.endswith("png")]

        audios = [mp3 for mp3 in os.listdir(self.audio_path)
                if mp3.endswith('.mp3')]

        print(images)
        print(audios)

    

    
