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

    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='file path of input file')
    args = parser.parse_args()

    ''' input_metadata holds the meta data from each entry in the input file
    is a list of dicts that will be used to build each video
    [ {link: <link>, n_entries: <n_entries>, video_name: <name> }, ...]
    '''
    input_metadata = [] 

    # Open the file from argument and build the list of meta data for each link to build videos 
    try:
        # Reading file, ignoring empty lines 
        with open(args.file, 'r') as f_in: 
            lines = list(line for line in (l.strip() for l in f_in) if line)

        #iterate through the lines of content and create the meta objects
        for entry in lines: 
            data = entry.split(' ') #split string at spaces... file format is: link num_comments title
            input_metadata.append({'url': data[0], 'n_entries': int(data[1]), 'title': data[2]})

    except FileNotFoundError:
        print('Invalid path to file')
        return 1

    

    # Loop through each video meta object and create videos 
    for video_meta in input_metadata: 
        print(video_meta)

        reddit_scraper = RedditScrape(video_meta['url'], video_meta['n_entries'])
        title, replies, authors = reddit_scraper.scrape_post()
        print(title)



    """
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
    Editor = VideoEditor(int(args.n_entries), args.video_name)
    Editor.create_movie()
    print('movie created')

    """

    return 0



if __name__ == '__main__':
    exit(main())


