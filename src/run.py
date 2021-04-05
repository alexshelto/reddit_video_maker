# This file will be the main driver function and run the entire progam
# This will import the Reddit Scraping Class and the Video Editing Class
#

# Used to handle command line arguments
import argparse

# Importing reddit scraping class 
from RedditScrape import RedditScrape


def main() -> int: 
    # Creating required command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='link of reddit post is required')
    parser.add_argument('n_entries', help='specify the number of replies to the post you want')
    # Parse the command line arguments
    args = parser.parse_args()

    '''
    this is where we will create a class instance of Reddit scraper and video maker
    Reddit class will return or create mp3 clips that will be used by the 
    video class afer 
    '''

    print("you want to make a video with the link: ", args.url)

    # Creating the reddit scraper class
    reddit_scraper = RedditScrape(args.url, int(args.n_entries))

    # Calling a function on the reddit scraper 
    reddit_scraper.scrape_post()


    return 0


if __name__ == '__main__':
    exit(main())


