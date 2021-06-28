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

    def __init__(self, audio_path='../audio/'):
        self.audio_path = audio_path
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








        '''
        # creating a unique mp3 file for each text to speech 
        # title first
        with open(self.path + 'title.mp3', 'wb') as f:
            # creating an audio of title and writing to file
            print(f'\n{submission.title}\n')
            clean_title = pre_processors.word_sub(submission.title)
            gtts(text=clean_title,lang='en').write_to_fp(f)
            # pushing encoded string to list of text used
            text_used.append(clean_title.encode('utf-8', 'replace'))

        # loop through each reply, turn to text to speech audio
        # then write to its on file 
        # first reply -> reply0.mp3, 2nd reply -> reply1.mp3 ....
        for i in range(0, len(comments)):
            data = reddit.comment(comments[i])
            print(f'top comment: {i+1}: {data.body}\n')
            # running pre process on words swapping naughty words for better ones
            clean_str = pre_processors.word_sub(data.body)
            # push text into list
            text_used.append(clean_str.encode('utf-8', 'replace'))
            # writing each text to speech to unique file 
            with open(self.path + 'reply' + str(i) + '.mp3', 'wb') as f:
                gtts(text=clean_str, lang='en').write_to_fp(f)
        '''
