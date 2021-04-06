# This is the class file for the reddit scraper
# This file will be called from the main file (run.py)
# This file will scrape comments/title, turn to text to speech files


#including the reddit api wrapper
import praw

#including the text to speech API: subject to change
from gtts import gTTS

# Pre process can let us exchange words. ie: exchanging curse words for others
from gtts.tokenizer import pre_processors
import gtts.tokenizer.symbols


#importing the config file
import sys
sys.path.append("../")
import config

import os


# Words that we will exchange for others in text scraping
# To ensure no terrible words are used in the video
gtts.tokenizer.symbols.SUB_PAIRS.append(
        ('fuck', 'F')
)


class RedditScrape:

    #Constructor
    def __init__(self, url, num_replies):
        """url: the link of the reddit post to scrape comments/title from
        num_replies: the number of top replies program will take to make video
        pause_time: time in between each replies audio
        path: path to folder: [audio] which stores audio files created or used
        """
        self.url = url
        self.num_replies = num_replies
        #self.pause_time = pause_time
        self.path = '../audio/' # Creating a directory to hold the audio in
         
    
    def scrape_post(self):
        """ Takes the link passed into the class constructor
        to scrape the reddit post for the title and the top comments
        then the function loops through the strings of text turning them into 
        a text to speech mp3 files and writes them to an mp3"""

        # Creating a list, will fill with title and comment text
        text_used = []
        # Creating a list of authors, used for post images
        authors = []

        # Creating an instance of reddit api
        reddit = praw.Reddit(
            client_id=config.PRAW_CONFIG['client_id'],
            client_secret=config.PRAW_CONFIG['client_secret'],
            user_agent=config.PRAW_CONFIG['user_agent'],
        )

        # Getting the submission (Post)
        submission = reddit.submission(url=self.url)

        submission.comment_sort = 'top' # Sorting the comments on the post to top voted
        submission.comments.replace_more(limit=0) #removing weird 'more' comments

        # Creating a list of the top n replies, n=num_replies. an argument to the class
        comments = submission.comments.list()[0:self.num_replies]

        # adding post author and replies authors
        authors.append(submission.author.name)
        for comment in comments:
            authors.append(comment.author.name)



        # Creating a folder to hold audio files in if it doesnt already exist
        try: 
            os.makedirs(self.path)
            print(f'directory: {self.path} created')
        except FileExistsError:
            print(f'directory: {self.path} already exists')
        

        # Getting blank audio file to add breaks in between text to speech audio
        f = open(self.path+'5-seconds-of-silence.mp3', 'rb')
        silence_5_sec = f.read()
        f.close()


        # Looping through the comments, creating text to speech audio
        # Then putting the text to speech audio into an mp3 file
        with open(self.path + 'reddit.mp3', 'wb') as f:
            # Creating an audio of title and writing to file
            print(f'\n{submission.title}\n')
            clean_title = pre_processors.word_sub(submission.title)
            gTTS(text=clean_title,lang='en').write_to_fp(f)
            # Pushing encoded string to list of text used
            #text_used.append(clean_title.encode('latin-1', 'replace'))

            text_used.append(clean_title.encode('utf-8', 'replace'))
            # adding a pause
            f.write(silence_5_sec)


            # Creating audio of the comments and adding to file
            for i in range(0,len(comments)):
                data = reddit.comment(comments[i])
                print(f'top comment: {i+1}: {data.body}\n')
                # Running pre process on words swapping naughty words for better ones
                clean_str = pre_processors.word_sub(data.body)
                # Push text into list
                text_used.append(clean_str.encode('utf-8', 'replace'))
                # Writing text to speech of string to the mp3 file
                gTTS(text=clean_str, lang='en').write_to_fp(f)
                # Adding a pause in audio
                self.add_pause(silence_5_sec, f)

        # Returns string: Title, list: replies
        return text_used[0], text_used[1:], authors


    def add_pause(self, five_sec_silence, output_file):
        '''function adds 5 seconds of silence to output file n times,
        specified by user in command line arg or default 5 sec between each text to speech'''
        output_file.write(five_sec_silence)
        return

