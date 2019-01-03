"""Bot's configuration settings."""
# Streamable credentials.
STREAMABLE_EMAIL = ''
STREAMABLE_PASSWORD = ''

# Reddit credentials.
CLIENT_ID = ''
CLIENT_SECRET = ''
USER_AGENT = 'Streamable mirroring bot (by /u/gourari)'
USERNAME = ''
PASSWORD = ''

SUBREDDIT_NAME = 'soccer'  # Without the prefix "r/".

COMMENT_AUTHOR = 'AutoModerator'  # The bot will look for comments
								  # made by this author and check if 
								  # it contain the keyword below in order
								  # to mirror and make a reply to that comment.

COMMENT_KEYWORD = 'Mirrors / Alternate angles'

ONLY_SPECIFIED_DOMAINS = True  # If True, only videos in DOMAINS will be mirrored.
							   # example: if a user post a youtube.com video
							   # 		  the bot will not mirror it even if 
							   #		  AutoModerator reply to that post.
							   		  
DOMAINS = [
	'twitter.com',
	'instagram.com',
	'facebook.com',
	'imgtc.com',
	'streamja.com',
	'imgtc.b-cdn.net',
	'clippituser.tv',
]
