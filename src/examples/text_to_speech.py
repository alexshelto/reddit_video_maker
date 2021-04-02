# This program will convert a text string into a text to speech audio file

from gtts import gTTS

def main() -> int:
    # A title, simulating scraping a title from a subreddit
    title = 'What’s a “boring” hobby that’s not boring at all?'

    # A comment, simulating scraping a comment to the post
    comment = "I do counted cross stitch. I'm not creative at all, but give me a coded pattern that creates a map (I always do maps - but you can make way more intricate things than you think if you invest the time) and I'm all over that shit. It's how I quit smoking."

    # Creating text to speech creation on those strings making mp3 data
    tts_entry1 = gTTS(title, lang='en', tld='ie')
    tts_entry2 = gTTS(comment, lang='en', tld='ie')

    # Write the mp3 data to a file to create audio object
    with open('reddit.mp3', 'wb') as f:
        tts_entry1.write_to_fp(f)
        tts_entry2.write_to_fp(f)

    return 0


if __name__ == '__main__':
    exit(main())
