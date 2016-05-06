import time
import thread
import tkMessageBox
import unicodedata

from irc import *
from bot_phrases import *


class Bot(object):
	def __init__(self):
		self._irc = IRC()
		self._irc.send_message("Hello")

		self._queue = []
		self._queue_update_hooks = []

		self._blacklist = [] #TODO: Add ability to save and load this list.

		#experimental phrases; this code is only temporary and will
		#be replaced with a better system for loading them dynamically.
		self._phrase_hooks = []

		self._phrase_hooks.append(BotPhrasePraiseFromOwner())
		self._phrase_hooks.append(BotPhraseLoveFromOwner())
		self._phrase_hooks.append(BotPhraseAngerFromOwner())

		self._last_reminder = None

		self._main_thread = thread.start_new_thread(self.__run, tuple())

	def add_queue_update_hook(self, fnc):
		self._queue_update_hooks.append(fnc)

	def __trigger_queue_update_hooks(self):
		queue = self.get_queue()
		for fnc in self._queue_update_hooks:
			fnc(queue)

	def __trigger_phase_hooks(self, sender, message):
		for hook in self._phrase_hooks:
			try:
				result = hook.test_phrase(sender, message)
				if result:
					self._irc.send_message(result)
					break
			except:
				pass

	def __run(self):
		while True:
			time.sleep(0.1)
			recv = self._irc.get_message()
			if recv:
				sender, message = self._irc.translate_message(recv)
				print "\""+sender+"\" : \""+message+"\""
				if message == "!play":
					if sender not in self._queue:
						if sender in self._blacklist:
							pass
						else:
							self._last_reminder = time.time()
							self._queue.append(sender)
							self._irc.send_message("/w " + sender + " You have been queued! You are #"+str(len(self._queue))+" in the line.")
							self.__trigger_queue_update_hooks()
					else:
						self._irc.send_message("/w " + sender + " You are already queued!")
				else:
					self.__trigger_phase_hooks(sender, message)

					if self._last_reminder == None:
						self._last_reminder = time.time()

			if self._last_reminder != None and time.time() - self._last_reminder > 240:
				self._last_reminder = None
				self._irc.send_message("Reminder: say \"!play\" if you want a chance to play! Also be sure I'm not blocked so you get my whispers.")

	def get_queue(self):
		queue = []
		i = 0
		while i < len(self._queue):
			normalized = unicodedata.normalize("NFKD", self._queue[i]).encode("ascii","ignore")
			queue.append(normalized)
			i += 1
		return queue

	def remove_from_queue(self, index):
		if index >= 0 and index < len(self._queue):
			self._queue.pop(index)
			self.__trigger_queue_update_hooks()

	def blacklist_player(self, index):
		if index >= 0 and index < len(self._queue):
			name = self._queue[index]
			self._irc.send_message(name + " has been blacklisted. They were naughty Kappa")
			self._irc.send_message("/w " + name + " You were blacklisted, come back another day when you're feeling more cooperative :/")
			self._blacklist.append(name)
			self.remove_from_queue(index)

	def startPlayers(self, room):
		if len(self._queue) == 0:
			tkMessageBox.showinfo("","There are not enough player's queued!")
			pass
		else:
			#simple check that the room code is good.
			if len(room) != 4 or not ROOM_PTN.match(room):
				tkMessageBox.showinfo("","The room code isn't right.")

			# Changing this min from 1 to x will change the number of players
			# that will get removed from the queue.
			i = min(1,len(self._queue))
			#tkMessageBox.showinfo("","Queuing "+str(i)+ " players!")
			while i > 0:
				i -= 1
				player = self._queue.pop(0)
				self._irc.send_message("/w "+player+" Time to play! The room code is \""+room+"\". Go to http://jackbox.tv/ and type this code into the textbox to join this match.")
			self.__trigger_queue_update_hooks()