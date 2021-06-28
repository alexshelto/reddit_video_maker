# This is the class file for the reddit scraper
# This file will be called from the main file (run.py)
# This file will scrape comments/title, turn to text to speech files


#including the reddit api wrapper
import praw


# Pre process can let us exchange words. ie: exchanging curse words for others
from gtts.tokenizer import pre_processors
import gtts.tokenizer.symbols

#importing the config file
import sys
import os
sys.path.append("../")


import config


# Words that we will exchange for others in text scraping
# To ensure no terrible words are used in the video
gtts.tokenizer.symbols.SUB_PAIRS.append(
        ('fuck', '*uck')
)


class RedditScrape:

    def __init__(self, url, num_replies):
        """url: the link of the reddit post to scrape comments/title from
        num_replies: the number of top replies program will take to make video
        path: path to folder: [audio] which stores audio files created or used
        """
        self.url = url
        self.num_replies = num_replies
        self.path = '../audio/' # Creating a directory to hold the audio in
         
    
    def scrape_post(self):
        """ Takes the link passed into the class constructor
        to scrape the reddit post for the title and the top comments
        then the function loops through the strings of text turning them into 
        a text to speech mp3 files and writes them to an mp3"""

        # Creating an instance of reddit api
        reddit = praw.Reddit(
            client_id=config.PRAW_CONFIG['client_id'],
            client_secret=config.PRAW_CONFIG['client_secret'],
            user_agent=config.PRAW_CONFIG['user_agent'],
        )

        text_used = [] #Creating list filled with strings of the title and all comment text
        authors = [] #Creating a list of authors from the post strings

        submission = reddit.submission(url=self.url) #Getting submission post
        submission.comment_sort = 'top' # Sorting the comments on the post to top voted
        submission.comments.replace_more(limit=0) #removing weird 'more' comments

        # Creating a list of the top n replies, n=num_replies. an argument to the class
        comments = submission.comments.list()[0:self.num_replies] #Change this to remove instance of getting "[deleted]" comments sometimes

        # adding post author and replies authors
        authors.append(submission.author.name)
        for comment in comments:
            try: 
                authors.append(comment.author.name)
            except AttributeError:
                authors.append('deleted')


    

        # Creating a folder to hold audio files in if it doesnt already exist
        try: 
            os.makedirs(self.path)
            print(f'directory: {self.path} created')
        except FileExistsError:
            print(f'directory: {self.path} already exists')


        clean_title = pre_processors.word_sub(submission.title)
        text_used.append(clean_title.encode('utf-8', 'replace'))
        

        for i in range(0, len(comments)):
            # Push cleaned string into text_used
            data = reddit.comment(comments[i])
            clean_str = pre_processors.word_sub(data.body)
            text_used.append(clean_str.encode('utf-8', 'replace'))


        '''
        # Creating a unique mp3 file for each text to speech 
        # Title first
        with open(self.path + 'title.mp3', 'wb') as f:
            # Creating an audio of title and writing to file
            print(f'\n{submission.title}\n')
            clean_title = pre_processors.word_sub(submission.title)
            gTTS(text=clean_title,lang='en').write_to_fp(f)
            # Pushing encoded string to list of text used
            text_used.append(clean_title.encode('utf-8', 'replace'))

        # Loop through each reply, turn to text to speech audio
        # Then write to its on file 
        # First reply -> reply0.mp3, 2nd reply -> reply1.mp3 ....
        for i in range(0, len(comments)):
            data = reddit.comment(comments[i])
            print(f'top comment: {i+1}: {data.body}\n')
            # Running pre process on words swapping naughty words for better ones
            clean_str = pre_processors.word_sub(data.body)
            # Push text into list
            text_used.append(clean_str.encode('utf-8', 'replace'))
            # Writing each text to speech to unique file 
            with open(self.path + 'reply' + str(i) + '.mp3', 'wb') as f:
                gTTS(text=clean_str, lang='en').write_to_fp(f)
        '''

        # Returns string: Title, list: replies
        return text_used[0], text_used[1:], authors


