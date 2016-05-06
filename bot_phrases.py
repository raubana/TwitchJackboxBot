import random
from cfg import CHAN, NICK


# Bot phrases are single, hook-based responses to messages
# posted by users in the chat. Below I've given three example
# phrase-types which are messages from the owner of the bot.


class BotPhrase(object):
	def __init__(self):
		pass

	def test_phrase(self, sender, message):
		return None


class BotPhrasePraiseFromOwner(object):
	def test_phrase(self, sender, message):
		message = message.lower()
		if sender == CHAN and NICK in message:
			if "thank you" in message or "thanks" in message:
				return random.choice(["no problem", ":3", "you're welcome"])
			if "good work" in message or "good job" in message or "nice job" in message or "nice work" in message:
				return random.choice(["<3", ":3", "thank you ^u^", "Thanks :D"])
			if "good bot" in message:
				return random.choice(["<3 <3 <3", "/me beams proudly", "^u^", "Thanks :D"])


class BotPhraseLoveFromOwner(object):
	def test_phrase(self, sender, message):
		message = message.lower()
		if sender == CHAN and NICK in message:
			if "love you" in message or "i love" in message:
				return random.choice(["<3", ":3", "love u 2 bb", "#^u^#", "beep boop, does not compute ;)"])


class BotPhraseAngerFromOwner(object):
	def test_phrase(self, sender, message):
		message = message.lower()
		if sender == CHAN and NICK in message:
			if "darn it" in message or "dang it" in message or "damn it" in message or "dammit" in message:
				return random.choice(["sorry ._.", "what I do??", ":< sorry"])
			if ("sit" in message and ("corner" in message or "time out" in message or "timeout" in message)):
				return random.choice(["k ._.", "/me sits down and pouts."])
			if "shutup" in message or "shut up" in message or "shut your" in message:
				return random.choice(["._.", "/me pouts.", ":x", ":<"])
