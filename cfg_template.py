import re

# Be sure to rename this file to "cfg.py" and to fill in the
# missing information below before running this project.

# You should use a different account than your main one for
# the bot, just in case it gets banned (hasn't happened yet
# to me, but it's a possible risk).

# One way to get your oauth code for the PASS variable:
# http://www.twitchapps.com/tmi/

HOST = "irc.twitch.tv"              			# the Twitch IRC server
PORT = 6667                         			# always use port 6667!
NICK = ""       	     						# your Twitch username, lowercase
PASS = ""										# your Twitch OAuth token
CHAN = "#" + ""                   					# the channel you want to join, lowercase

MESSAGE_DELAY = 0.5
CHAT_MSG_PTN = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
ROOM_PTN = re.compile(r"[A-Z][A-Z][A-Z][A-Z]")