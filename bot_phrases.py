import random, time
from cfg import CHAN, NICK


# Bot phrases are single, hook-based responses to messages
# posted by users in the chat. Below I've given three example
# phrase-types which are messages from the owner of the bot.


class BotPhrase(object):
	def __init__(self):
		pass

	def test_phrase(self, sender, message):
		return None


class BotPhraseGreeting(BotPhrase):
	def __init__(self):
		super(BotPhraseGreeting, self).__init__()
		self.people_already_greeted = {}

	def test_phrase(self, sender, message):
		t = time.time()
		if sender not in self.people_already_greeted or t - self.people_already_greeted[sender] > 300:
			message = message.lower()
			if "hello" in message or "hey" in message or "sup" in message or "hi" in message or "salutation" in message or "greeting" in message or "hoi" in message:
				return random.choice(["Hi, "+sender, "Hello!", "Welcome :3", "Greetings, "+sender, "Hi there", "Sup"])

		self.people_already_greeted[sender] = t


class BotPhrasePraise(BotPhrase):
	def __init__(self):
		super(BotPhrasePraise, self).__init__()
		self.last_response = 0

	def test_phrase(self, sender, message):
		t = time.time()
		if t - self.last_response > 30:
			message = message.lower()
			if NICK in message:
				output = None
				if "thank you" in message or "thanks" in message:
					output = random.choice(["no problem", ":3", "you're welcome"])
				elif "good work" in message or "good job" in message or "nice job" in message or "nice work" in message:
					output = random.choice(["<3", ":3", "thank you ^u^", "Thanks :D"])
				elif "good bot" in message:
					output = random.choice(["<3 <3 <3", "/me beams proudly", "^u^", "Thanks :D"])
				if output != None:
					self.last_response = t
					return output



class BotPhraseLoveFromOwner(BotPhrase):
	def test_phrase(self, sender, message):
		message = message.lower()
		if sender == CHAN[1:] and NICK in message:
			if "love you" in message or "i love" in message:
				return random.choice(["<3", ":3", "love u 2 bb", "#^u^#", "beep boop, does not compute ;)"])
			if "best" in message:
				return random.choice(["<3", ":3", "#^u^#", "Kappa"])

class BotPhraseAngerFromOwner(BotPhrase):
	def test_phrase(self, sender, message):
		message = message.lower()
		if sender == CHAN[1:] and NICK in message:
			if "darn it" in message or "dang it" in message or "damn it" in message or "dammit" in message:
				return random.choice(["sorry ._.", "what I do??", ":< sorry"])
			if ("sit" in message and ("corner" in message or "time out" in message or "timeout" in message)):
				return random.choice(["k ._.", "/me sits down and pouts."])
			if "shutup" in message or "shut up" in message or "shut your" in message:
				return random.choice(["._.", "/me pouts.", ":x", ":<"])
