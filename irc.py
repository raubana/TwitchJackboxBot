from cfg import *
import socket
import time
import thread


class IRC(object):
	def __init__(self):
		self._connected = False

		self._socket = socket.socket()
		self.__connect()
		self._incoming_message_buffer = []
		self._outgoing_message_buffer = []

		self._listen_thread = thread.start_new_thread(self.__listen, tuple())
		self._transmit_thread = thread.start_new_thread(self.__transmit, tuple())

	def __connect(self):
		self._socket.connect((HOST, PORT))
		self._socket.send("PASS {}\r\n".format(PASS).encode("utf-8"))
		self._socket.send("NICK {}\r\n".format(NICK).encode("utf-8"))
		self._socket.send("JOIN {}\r\n".format(CHAN).encode("utf-8"))

		self._connected = True

	def __listen(self):
		print "LISTENING"
		while True:
			while self._connected:
				try:
					recv = self._socket.recv(1024).decode("utf-8")
				except:
					recv = None
				if not recv:
					print "-Connection dropped."
					self.close()
				else:
					if recv == "PING :tmi.twitch.tv\r\n":
						self.__send_message("PONG :tmi.twitch.tv\r\n".encode("utf-8"), True)
					else:
						print(recv)
						self._incoming_message_buffer.append(recv)
			print "-LISTEN THREAD EXITING..."
			thread.exit()

	def __transmit(self):
		print "TRANSMITTING"
		while self._connected:
			time.sleep(MESSAGE_DELAY)
			if len(self._outgoing_message_buffer) > 0:
				message = self._outgoing_message_buffer.pop(0)
				self.__send_message(message)
		print "-TRANSMIT THREAD EXITING..."
		thread.exit()

	def send_message(self, msg):
		self._outgoing_message_buffer.append(msg)

	def get_message(self):
		if len(self._incoming_message_buffer) > 0:
			return self._incoming_message_buffer.pop(0)
		return None

	def translate_message(self, msg):
		username = re.search(r"\w+", msg).group(0) # return the entire match
		message = CHAT_MSG_PTN.sub("", msg)
		message = message.strip()
		return username, message

	def __send_message(self, msg, raw = False):
		print("SENDING " + msg)
		if raw:
			self._socket.send(msg)
		else:
			self._socket.send("PRIVMSG {} :{}\r\n".format(CHAN, msg))

	def close(self):
		self._connected = False
		try: self._socket.shutdown(socket.SHUT_RDWR)
		except: pass
		try: del self._socket
		except: pass
