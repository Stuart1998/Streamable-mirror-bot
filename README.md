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
  - Create a discord bot app:
    - go to https://discordapp.com/developers/applications/ and click `Create an application` https://i.imgur.com/nNRQat0.png
    - now you have a discord client id https://i.imgur.com/G7cf5Y5.png
    - click the `Bot` tab on the left then click `Add Bot` and `Yes, do it!`
    - now you have a discord token https://i.imgur.com/O8Jztqz.png
    - add that discord client id to this link (https://discordapp.com/oauth2/authorize?scope=bot&permissions=o&client_id=) and open it
    - select the server you want the bot to operate on and click `Authorize` https://i.imgur.com/O4P5SH0.png
  - Download `bot.py`
  - Open it with a text editor (keep the single quotes in the following steps):
    - line 10 put the discord token.
    - line 11 put the server channel id that you want the bot to send messages to. https://i.imgur.com/ayewLYU.png
    - line 13 put the reddit client id.
    - line 14 put the reddit client secret.
    - line 16 put the reddit username of the bot's account.
    - line 17 put the reddit password of the bot's account.
    - line 20 specify the keywords that the bot should look for (keywords should be between single-quotes and comma seperated).
    - line 21 specify the rate in which the bot should check (default is 30 seconds).
  - save it.
  - run `bot.py` (double click or open the command line/terminal in the file directory and type *python3 bot.py*).
**Note**: Videos that are over 10 minutes will not be mirrored.
## License
  [The MIT License](https://opensource.org/licenses/MIT)
