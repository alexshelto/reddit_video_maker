import praw
import config



# Main driver function for software
def main() -> int:

    #Creating a reddit api instance 
    reddit = praw.Reddit(
        client_id=config.PRAW_CONFIG['client_id'],
        client_secret=config.PRAW_CONFIG['client_secret'],
        user_agent=config.PRAW_CONFIG['user_agent'],
    )

    # Looping a subreddit
    for submission in reddit.subreddit("learnpython").hot(limit=10):
        print(submission.title)


    return 0






# Calling the main function
if __name__ == '__main__':
    exit(main())
