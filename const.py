"""Bot's constants."""
UPLOAD = 'https://api.streamable.com/import?url={url}'
VIDEO_URL = 'https://streamable.com/{shortcode}'
HEADERS = {'User-Agent': 'Streamable mirroring reddit bot'}
REPLY_MESSAGE = ('[Streamable Mirror]({link})\n\n'
				 '*I am a bot, and this action was performed automatically.*')
TIMEOUT = 10
LOG_MSG = 'submission: {} mirror: {}'
LOG_FILE = 'logs.log'
