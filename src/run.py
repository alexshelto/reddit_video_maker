# This file will be the main driver function and run the entire program
# This will import the Reddit Scraping Class and the Video Editing Class

import argparse  # Used to handle command line arguments

from RedditScrape import RedditScrape  # Importing reddit scraping class to acquire posts and authors

from TextToSpeech import TextToSpeech  # Importing tts class to make mp3 of posts

from ImageCreator import ImageCreator  # Generates images of posts

from VideoEdit import VideoEditor  # Edits all the tts mp3 and Images into a mp4 video


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='file path of input file')
    args = parser.parse_args()

    ''' input_metadata holds the meta data from each entry in the input file
    is a list of dicts that will be used to build each video
    [ {link: <link>, n_entries: <n_entries>, title: <name> }, ...]
    '''
    input_metadata = []

    # Open the file from argument and build the list of meta data for each link to build videos 
    try:
        # Reading file, ignoring empty lines 
        with open(args.file, 'r') as f_in:
            lines = list(line for line in (l.strip() for l in f_in) if line)

        # iterate through the lines of content and create the meta objects
        for entry in lines:
            data = entry.split(' ', 2)  # split string at spaces... file format is: link num_comments title
            whitelist = set(
                'abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')  # maybe regex could be used instead
            data[2] = ''.join(filter(whitelist.__contains__, data[2]))
            input_metadata.append({'url': data[0], 'n_entries': int(data[1]), 'title': data[2]})

    except FileNotFoundError:
        print('Invalid path to file')
        return 1

    # Loop through each video meta object and create videos
    for video_meta in input_metadata:
        print(video_meta)

        reddit_scraper = RedditScrape(video_meta['url'], video_meta['n_entries'])

        # Returns 2 lists of strings, [all posts] [authors of posts]
        # index 0 of both are associated with the title, the rest are replies to the thread
        posts, authors = reddit_scraper.scrape_post()

        try:
            assert (len(posts) == len(authors))
            print(len(posts))

        except AssertionError:
            print(f'''Something went wrong in the Reddit Scrape...
                    length of posts: {str(len(posts))} != len authors: {str(len(authors))}
                    Exiting Program.''')
            return -1

        for i, post in enumerate(posts):
            print(f'{i}: {post}')

        # Text to speech 
        tts = TextToSpeech()  # Creating tts class
        tts.create_tts(posts)  # Creating all tts mp3 files for video 

        # Image Creation
        # Creating image for title 
        ImageCreator.create_image_for(posts[0], authors[0], 'title')

        # Creating image post for the replies: reply0.jpg, reply1.jpg, ...
        for i in range(1, len(posts)):
            ImageCreator.create_image_for(posts[i], authors[i], f'reply{str(i - 1)}')

        # Creating a Video Editing object
        # Passing n_entries + 1, for # of images, since we have title + n replies

        Editor = VideoEditor(int(video_meta['n_entries']), video_meta['title'])
        Editor.create_movie()
        print('movie created')

    return 0


if __name__ == '__main__':
    exit(main())
