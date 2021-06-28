# TextToSpeech.py
# Called in run.py after RedditScrape.py has scraped all of the content 
# Creates an audio file for each scraped post 
#
#





#including the text to speech API: subject to change
from gtts import gTTS

import os
import sys
sys.path.append("../")


class TextToSpeech:

    def __init__(self):
        self.audio_path = '../audio/' 
        self.create_dir() # Creates the directory to hold audio if not already specified 


    def create_dir(self):
        '''Creates the dir to hold the audio files if it doesnt already exist'''
        try: 
            os.makedirs(self.audio_path)
            print(f'directory: {self.audio_path} created')
        except FileExistsError:
            pass

    
    def create_tts(self, posts):
        '''Takes the list of posts and creates text to speech audio for each one
        places them in the audio_path directory...
        the 0th index of posts is the title so we explicitly name it title.mp3'''

        # Creating the title tts first
        with open(f'{self.audio_path}title.mp3', 'wb') as f:
            gTTS(text=posts[0], lang='en').write_to_fp(f)

        # Creating tts for the replies next
        for i, reply in enumerate(posts[1:]):
            # Saving tts of replies as: reply0.mp3, reply1.mp3, ... , replyn.mp3
            with open(f'{self.audio_path}reply{str(i)}.mp3', 'wb') as f:
                gTTS(text=reply, lang='en').write_to_fp(f)

