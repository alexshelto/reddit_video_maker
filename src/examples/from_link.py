import praw
import sys
import argparse # command line argument parser

sys.path.append("../")
import config


reddit = praw.Reddit(
    client_id=config.PRAW_CONFIG['client_id'],
    client_secret=config.PRAW_CONFIG['client_secret'],
    user_agent=config.PRAW_CONFIG['user_agent'],
)

def main() -> int: 

    # Creating an argument parser and an argument for the link
    parser = argparse.ArgumentParser()
    parser.add_argument('link', help='the link of the post')
    args = parser.parse_args() # Collecting arguments 


    # Creating reddit api instance
    reddit = praw.Reddit(
        client_id=config.PRAW_CONFIG['client_id'],
        client_secret=config.PRAW_CONFIG['client_secret'],
        user_agent=config.PRAW_CONFIG['user_agent'],
    )

    # Creating an instance of a reddit thread? 
    submission = reddit.submission(url=args.link)
    print(f'Submission title: \n{submission.title}')

    return 0






if __name__ == '__main__':
    exit(main())

