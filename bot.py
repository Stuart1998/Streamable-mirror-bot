import logging
import time

import praw
import requests

from const import *
from config import *


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
		time.sleep(5)
		r = requests.head(video_link, timeout=TIMEOUT)
		if r.status_code == 200:
			return video_link
		elif r.status_code == 404:
			return None
	elif r.status_code == 404:
		raise ValueError('Invalid URL.')


def main():
	print(' Running...', end='\r')
	reddit = praw.Reddit(client_id=CLIENT_ID,
						 client_secret=CLIENT_SECRET,
						 user_agent=USER_AGENT,
						 username=USERNAME,
						 password=PASSWORD)
	subreddit = reddit.subreddit(SUBREDDIT_NAME)
	for comment in subreddit.stream.comments(skip_existing=True, pause_after=0):
		if (comment is None or 
				comment.author != COMMENT_AUTHOR or
				COMMENT_KEYWORD not in comment.body):
			continue
		submission = comment.submission
		shortlink = submission.shortlink
		if not ONLY_SPECIFIED_DOMAINS or submission.domain in DOMAINS:
			try:
				link = mirror_url(submission.url)
				if link is None:
					logger.info(LOG_MSG.format(shortlink, 'VIDEO OVER 10 MIN or COULD NOT PROCESS FILE'))
					continue
				reply = REPLY_MESSAGE.format(link=link)
				comment.reply(reply)
				logger.info(LOG_MSG.format(shortlink, link))
			except ValueError:
				logger.info(LOG_MSG.format(shortlink, 'INVALID LINK'))
			except requests.exceptions.Timeout:
				logger.exception(LOG_MSG.format(shortlink, 'TIMEOUT\n'))


if __name__ == '__main__':
	logger = logging.getLogger(__name__)
	logger.setLevel(logging.DEBUG)
	formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
	file_handler = logging.FileHandler(LOG_FILE)
	file_handler.setFormatter(formatter)
	logger.addHandler(file_handler)
	try:
		main()
	except Exception:
		logger.exception('Unexpected error\n')
		input('The bot has stopped due to an error, check "{}".'.format(LOG_FILE))
