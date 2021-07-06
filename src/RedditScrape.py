# RedditScrape.py
# Last edited: June 28th 2021
# 
# Called from run.py
# Given a URL and an argument for number of posts to scrape, Class will connect to reddit API
# and scrape the content from the post returning a title, authors, and replies
#


# importing the config.py file to connect to PRAW
from config import reddit_api

# Pre process can let us exchange words. ie: exchanging curse words for others
from gtts.tokenizer import pre_processors
import gtts.tokenizer.symbols

import sys

sys.path.append("../")

# Words that we will exchange for others in text scraping
# To ensure no terrible words are used in the video
gtts.tokenizer.symbols.SUB_PAIRS.append(
    ('fuck', '*uck')
)


class RedditScrape:

    def __init__(self, url, num_replies):
        '''url: the link of the reddit post to scrape comments/title from
        num_replies: the number of top replies program will take to make video
        path: path to folder: [audio] which stores audio files created or used'''

        self.url = url
        self.num_replies = num_replies
        self.path = '../audio/'  # Creating a directory to hold the audio in

    def scrape_post(self):
        '''Takes the link passed into the class constructor
        to scrape the reddit post for the title and the top comments
        then the function loops through the strings of text turning them into 
        a text to speech mp3 files and writes them to an mp3'''

        # Creating an instance of reddit api
        reddit = reddit_api()

        text_used = []  # Creating list filled with strings of the title and all comment text
        authors = []  # Creating a list of authors from the post strings

        submission = reddit.submission(url=self.url)  # Getting submission post
        submission.comment_sort = 'top'  # Sorting the comments on the post to top voted
        submission.comments.replace_more(limit=0)  # removing weird 'more' comments

        # Creating a list of the top n replies, n=num_replies. an argument to the class
        comments = submission.comments.list()[0:self.num_replies]

        # removes deleted comments
        for top_level_comment in comments:
            if "[deleted]" in top_level_comment.body:
                comments.remove(top_level_comment)
                comments.append(submission.comments.list()[self.num_replies + 1])
                self.num_replies += 1

        # adding post author and replies authors
        authors.append(submission.author.name)
        for comment in comments:
            try:
                authors.append(comment.author.name)
            except AttributeError:
                authors.append('deleted')

        clean_title = pre_processors.word_sub(submission.title)
        text_used.append(clean_title)

        for i in range(0, len(comments)):
            # Push cleaned string into text_used
            data = reddit.comment(comments[i])
            clean_str = pre_processors.word_sub(data.body)
            text_used.append(clean_str)  # .encode('utf-8', 'replace'))

        # Returns text used: [title & replies], and [authors]
        return text_used, authors
