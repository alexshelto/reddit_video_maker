# Obtain Praw credentials and add your client id, secret, and user agent to environment variables
# For help try visiting: https://www.jcchouinard.com/get-reddit-api-credentials-with-praw/
#              and: reddit.com/prefs/apps
import os
import praw


def reddit_api():
    reddit = praw.Reddit(
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("CLIENT_SECRET"),
        user_agent=os.getenv("USERNAME"))

    return reddit
