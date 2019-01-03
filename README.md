# Streamable-mirror-bot
A bot for Reddit that mirror videos from posts of specified domains to Streamable and replies with the link.

This branch is specif use case for r/soccer, the bot will listen to comments made on the subreddit and will mirror video in posts that the AutoModerator replied to with a specific keyword, it will then reply to that comment with the link to the mirror.
## Requirements:
- [Python](https://www.python.org/) 3+
- Third party libraries:
  - [PRAW](https://praw.readthedocs.io/en/latest/getting_started/installation.html) 6+ (*pip install praw*)
  - [Requests](http://docs.python-requests.org/en/master/) (*pip install requests*)
## How to run:
  After installing the requirements:
  - Create a reddit script app:
    - go to https://www.reddit.com/prefs/apps/ and click `are you a developer? create an app...` or `create another app...`
    - name your app, select script and put a redirect uri (http://localhost:8080 will work) and click `create app` https://i.imgur.com/6L8YNiJ.png
    - now you have a reddit client id (under personal use script) and a reddit client secret. https://i.imgur.com/lQdqav0.png
  - [Create a Streamable account](https://streamable.com/signup) and verify the email.
  - Download the following files and place them in the same folder:
    - `bot.py`
    - `const.py`
    - `config.py`
    - `reply message.txt`
  - Open `config.py` with a text editor and add the required credentials.
  - Save it.
  - Run `bot.py` (double click or open the command line/terminal in the file directory and type *python3 bot.py*).
  
**Notes**:
  - Videos that are over 10 minutes will not be mirrored. 
## License
  [The MIT License](https://opensource.org/licenses/MIT)
