# This clas will hold the class that edits the images into video
#TODO: Once complete, remove global import and only import required

from moviepy.editor import * # movie editor 
import os  # used for some file grabbing
from PIL import Image # Image library

class VideoEditor:
    def __init__(self,num_replies, video_name):
        self.num_replies = num_replies
        self.video_name = video_name
        self.image_path = '../images/'
        self.audio_path = '../audio/'
        self.save_path = '../edited_videos/'

        self.create_dir() # Creates the edited videos dir if it doesnt exist

        print(self.num_replies)


    def create_dir(self):
        '''Creates the dir to hold the edited video if it doesnt already exist'''
        try: 
            os.makedirs(self.save_path)
            print(f'directory: {self.save_path} created')
        except FileExistsError:
            pass

    def create_movie(self):
        '''
        Creates a .mp4 file for every text to speech and post
        will then combine every mp4 file for entire video
        can add transitions this way
        '''
        clips = [] # clips are mp4 clips to be combined to make entire movie
        clip_count = 0
        

        # Create audio file and image file, then combine and add to list of clips
        title_audio = AudioFileClip(self.audio_path + 'title.mp3')
        title_clip = ImageClip(self.image_path + 'title.jpeg').set_duration(title_audio.duration+0.5)
        title_mp4 = concatenate([title_clip], method="compose")
        new_audioclip = CompositeAudioClip([title_audio])

        title_mp4.audio = new_audioclip
        clips.append(title_mp4)

        # Loop through the rest of posts doing same thing above
        for i in range(0, self.num_replies):
            tmp_audio = AudioFileClip(f'{self.audio_path}reply{i}.mp3')
            tmp_dur = tmp_audio.duration
            tmp_clip = ImageClip(f'{self.image_path}reply{i}.jpeg').set_duration(tmp_dur + 0.5)
            tmp_mp4 = concatenate([tmp_clip], method='compose')
            tmp_mp3 = CompositeAudioClip([tmp_audio])
            tmp_mp4.audio = tmp_mp3

            clips.append(tmp_mp4)
            

        # Combina all clips, and combine into master video
        final_vid = concatenate(clips, method='compose')

        final_vid.write_videofile(f'{self.save_path}{self.video_name}.mp4',
          fps=10,
          codec='libx264',
          audio_codec='aac',
          temp_audiofile='temp-audio.m4a',
          remove_temp=True
        )

        


    
