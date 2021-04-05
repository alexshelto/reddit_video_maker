# This is the class file for the reddit scraper
# This file will be called from the main file (run.py)
# This file will scrape comments/title, turn to text to speech files


#including the reddit api wrapper
import praw


#importing the config file
import sys
sys.path.append("../")
import config


class RedditScrape:

    #Constructor
    def __init__(self, url, num_replies):
        self.url = url
        self.num_replies = num_replies
         
    
    def scrape_post(self):
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

        
        # Outputting title and top n comments
        print(f'\n{submission.title}\n')

        for i in range(0,len(comments)):
            comment = reddit.comment(comments[i])
            print(f'top comment: {i+1}: {comment.body}\n')



    
    def hi(self):
         print("hello ")
