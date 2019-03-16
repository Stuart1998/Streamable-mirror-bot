"""Reddit Streamavble mirroring bot.
A reddit bot that mirror videos from posts of specified domains
to Streamable and replies with the link."""
import logging
import time

import praw
import prawcore
import requests

from config import *
from const import *


def mirror_url(url):
	"""Create a video on Streamable from url and return it link.

	Parameters
	-----------
	url : string
		URL of the video source.
	
	Raises
	-------
	ValueError
		the url provided is invalid.
	"""
	r = requests.get(UPLOAD.format(url=url), headers=HEADERS, timeout=TIMEOUT,
				 	 auth=(STREAMABLE_EMAIL, STREAMABLE_PASSWORD))
	if r.status_code == 200:
		video_link = VIDEO_URL.format(shortcode=r.json()['shortcode'])
		time.sleep(2)
		r = requests.head(video_link)
		if r.status_code == 200:
			return video_link
		elif r.status_code == 404:
			return None
	elif r.status_code == 404:
		raise ValueError('Invalid URL.')


def check_permissions():
	mod = subreddit.moderator(reddit.user.me())
	if (STICKY_COMMENT and 
			(not mod or not any(perm in mod[0].mod_permissions 
								for perm in ['posts', 'all']))):
		print('WARNING: To sticky the reply comment, the bot must be a '
			  'moderator on the subreddit and have posts permissions.\n')


def video_url(url, domain):
	if domain == 'v.redd.it':
		 r = requests.post('https://vredd.it/ajax_process.php',
		 				   data={'url': url})
		 return 'https://vredd.it/files/{}.mp4'.format(url[18:])
	return url


def main():
	check_permissions()
	print(' Running...', end='\r')
	for submission in subreddit.stream.submissions(skip_existing=True):
		shortlink = submission.shortlink
		if submission.domain in DOMAINS:
			try:
				link = mirror_url(video_url(submission.url, submission.domain))
				if link is None:
					logger.info(LOG_MSG.format(shortlink, 'VIDEO OVER 10 MIN'))
					continue
				reply = REPLY_MESSAGE.replace('{link}', link)
				comment = submission.reply(reply)
				logger.info(LOG_MSG.format(shortlink, link))
				if STICKY_COMMENT:
					comment.mod.distinguish(how='yes', sticky=True)
			except ValueError:
				logger.info(LOG_MSG.format(shortlink, 'INVALID LINK'))
			except requests.exceptions.Timeout:
				logger.exception(LOG_MSG.format(shortlink, 'TIMEOUT\n'))
			except prawcore.exceptions.Forbidden:
				logging.error('Unable to sticky comment, permisson not granted.')


if __name__ == '__main__':
	LOG_MSG = 'submission: {} mirror: {}'
	LOG_FILE = 'logs.log'
	logger = logging.getLogger(__name__)
	logger.setLevel(logging.DEBUG)
	formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
	file_handler = logging.FileHandler(LOG_FILE)
	file_handler.setFormatter(formatter)
	logger.addHandler(file_handler)
	try:
		with open(REPLY_MESSAGE_FILE) as f:
			REPLY_MESSAGE = f.read().strip()
			if not REPLY_MESSAGE:
				raise EOFError
		reddit = praw.Reddit(client_id=CLIENT_ID,
						 client_secret=CLIENT_SECRET,
						 user_agent=USER_AGENT,
						 username=USERNAME,
						 password=PASSWORD)
		subreddit = reddit.subreddit(SUBREDDIT_NAME)
		main()
	except (FileNotFoundError, EOFError):
		input('"{}" not found or empty.'.format(REPLY_MESSAGE_FILE))
	except Exception:
		logger.exception('Unexpected error\n')
		input('The bot has stopped due to an error, check "{}".'.format(LOG_FILE))
