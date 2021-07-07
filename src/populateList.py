from config import reddit_api

reddit = reddit_api()
SUBREDDIT = 'AskReddit'  # Replace with the name of the subreddit to pull submissions and comments from
NUM_COMMENTS = 50  # Replace with desired number of comments
NUM_ENTRIES = 5  # Replace with number of videos/links desired

list_file = open(r"list.txt", "w+")

for submission in reddit.subreddit(SUBREDDIT).top("week", limit=NUM_ENTRIES):
    list_entry = submission.url + " " + str(NUM_COMMENTS) + " " + submission.title + '\n'
    list_file.write(list_entry)

list_file.close()
