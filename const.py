"""Bot's constants."""

UPLOAD = 'https://api.streamable.com/import?url={url}'
RETREIVE = 'https://api.streamable.com/videos/{shortcode}'
VIDEO_URL = 'https://streamable.com/{shortcode}'
HEADERS = {'User-Agent': 'Streamable mirroring reddit bot'}
REPLY_MESSAGE = ('Streamable mirror: {link}\n\n'
				 '*I am a bot, and this action was performed automatically. '
				 'Please [contact the moderators of this subreddit]'
				 '(https://www.reddit.com/message/compose?to=%2Fr%2F{sub_name})'
				 ' if you have any questions or concerns.*')
TIMEOUT = 5
LOG_MSG = 'submission: {} mirror: {}'
LOG_FILE = 'logs.log'