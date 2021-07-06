# reddit_video_maker
This project will find popular Reddit threads and convert them into a text-to-speech videos. 

1. Find popular reddit threads worthy of being converted to threads using reddit api and some type of web scraping.

2. Convert top threads into static images, convert top thread title's to TTS using text-to-speech api. 

3. Convert answer of threads into static image, read outloud with text-to-speech
  - repeat with all relevant & interesting answers to the question 

4. String Question image with text-to-speech & string Answers image with text-to-speech into a video using video editing api. 



# Usage
* Use virtual environment and download requirements
* Create config.py folder in src/
  - Generate Praw API key and list the details there
  - see: https://www.reddit.com/prefs/apps and https://www.jcchouinard.com/get-reddit-api-credentials-with-praw/
* Post reddit links inside of src/list.txt
* run `python run.py list.txt`

## Example list.txt file
```
<reddit post link> <number of comments to scrape> <title of mp4 video>
<reddit post link> <number of comments to scrape> <title of mp4 video>
...
```

## How it works
* Uses a Reddit api to scrape Post and top comments from Reddit r/askreddit posts
* Scrapes the content from post/comments to create images for each post and combine them into an mp4 file
* Puts the text into text to speech to create mp3 file for soundtrack behind clips

