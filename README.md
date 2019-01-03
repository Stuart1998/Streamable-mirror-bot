# Streamable-mirror-bot
A bot for Reddit that mirror videos from posts of specified domains to Streamable and replies with the link.
## Requirements:
- [Python](https://www.python.org/) 3+
- Third party libraries:
  - [PRAW](https://praw.readthedocs.io/en/latest/getting_started/installation.html) (*pip install praw*)
  - [Requests](http://docs.python-requests.org/en/master/) (*pip install requests*)
## How to run:
  After installing the requirements:
  - Create a reddit script app:
    - go to https://www.reddit.com/prefs/apps/ and click `are you a developer? create an app...` or `create another app...`
    - name your app, select script and put a redirect uri (http://localhost:8080 will work) and click `create app` https://i.imgur.com/6L8YNiJ.png
    - now you have a reddit client id (under personal use script) and a reddit client secret. https://i.imgur.com/lQdqav0.png
  - [Create a Streamable account](https://streamable.com/signup) and verify the email.
  - Download the following files and place them in the same folder:
    - bot.py
    - const.py
    - config.py
  - Open `config.py` with a text editor and add the required credentials.
  - Save it.
  - Run `bot.py` (double click or open the command line/terminal in the file directory and type *python3 bot.py*).
  
**Notes**: 
  - If STICKY_COMMENT is set to `True` (line 16), the bot need to be a moderator on the subreddit and have posts permission.
  - The reply message can be edited in `reply message.txt`.
  - Videos that are over 10 minutes will not be mirrored.
## Version:
  - 0.0.2 (03/01/2019):
    - Added an option to make the comment stickied (requires mod and posts permission).
    - Added `reply message.txt` to make editing the reply message easier.
  - 0.0.1 (30/12/2018) 
## License
  [The MIT License](https://opensource.org/licenses/MIT)
