# This file will be the main driver function and run the entire progam
# This will import the Reddit Scraping Class and the Video Editing Class

# Used to handle command line arguments
import argparse
# Importing reddit scraping class 
from RedditScrape import RedditScrape
# Importing the video editing class
from VideoEdit import VideoEditor
# Importing some utility functions from utils.py
from utils import utils


def main() -> int: 
    """Main driver functio that runs the entire program
    parses command line arguments and creates a reddit scrape and video edit class"""
    # Creating required command line arguments
    parser = argparse.ArgumentParser()
    # Adding required argument: url of the reddit link
    parser.add_argument('url', help='link of reddit post is required')
    # Adding required argument, number of entries (comments) to read
    parser.add_argument('n_entries', help='specify the number of replies to the post you want')
    # Parse the command line arguments
    args = parser.parse_args()
        

    '''
    this is where we will create a class instance of Reddit scraper and video maker
    Reddit class will return or create mp3 clips that will be used by the 
    video class afer 
    '''

    # Creating the reddit scraper class
    reddit_scraper = RedditScrape(args.url, int(args.n_entries))

    # Scrapes reddit post of title and replies, makes text to speech audio, and returns strings used
    # string title, list of replies, and a list of authors: [title author, reply 1 author, reply2 author ,... ]
    title, replies, authors = reddit_scraper.scrape_post()
    
    title_author = authors[0]   #the title author was stored in index 0
    reply_authors = authors[1:] #the rest of the indexes are reply author names

    # Creating an image for the title
    utils.create_image_for(title, title_author, 'title')
    # Creating image post for the replies
    for i in range(0, len(replies)):
        img_name = 'reply'+str(i)
        utils.create_image_for(replies[i],reply_authors[i], img_name)


    # Creating a Video Editing object
    # Passing n_entries + 1, for # of images, since we have title + n replies
    Editor = VideoEditor(int(args.n_entries) + 1)
    Editor.create_movie()

    return 0



if __name__ == '__main__':
    exit(main())


