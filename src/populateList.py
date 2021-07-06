from config import reddit_api

reddit = reddit_api()
SUBREDDIT = 'AskReddit'
NUM_COMMENTS = 12
NUM_ENTRIES = 5

list_file = open(r"list.txt", "w+")

for submission in reddit.subreddit(SUBREDDIT).top("day", limit=NUM_ENTRIES):
    list_entry = submission.url + " " + str(NUM_COMMENTS) + " " + submission.title + '\n'
    list_file.write(list_entry)

list_file.close()
