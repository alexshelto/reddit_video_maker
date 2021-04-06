# This file will be the main driver function and run the entire progam
# This will import the Reddit Scraping Class and the Video Editing Class



# Used to handle command line arguments
import argparse
# Importing reddit scraping class 
from RedditScrape import RedditScrape




def main() -> int: 
    """Main driver functio that runs the entire program
    parses command line arguments and creates a reddit scrape and video edit class"""

    # Creating required command line arguments
    parser = argparse.ArgumentParser()
    # Adding required argument: url of the reddit link
    parser.add_argument('url', help='link of reddit post is required')
    # Adding required argument, number of entries (comments) to read
    parser.add_argument('n_entries', help='specify the number of replies to the post you want')
    #adding an optional argument: -p, pause time in between posts (sec). default is 2
    parser.add_argument('-p', '--pause', help='config file')
    # Parse the command line arguments
    args = parser.parse_args()


    # If pause time is not entered, (optional) default is 2
    pause_time = 2
    if (args.pause is not None): 
        pause_time = args.pause
        

    '''
    this is where we will create a class instance of Reddit scraper and video maker
    Reddit class will return or create mp3 clips that will be used by the 
    video class afer 
    '''

    print("you want to make a video with the link: ", args.url)

    # Creating the reddit scraper class
    reddit_scraper = RedditScrape(args.url, int(args.n_entries), int(pause_time))

    # Calling a function on the reddit scraper 
    reddit_scraper.scrape_post()


    return 0


if __name__ == '__main__':
    exit(main())


