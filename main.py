from bot import *
import time
import Tkinter


class Application(Tkinter.Frame):
	def __init__(self, master=None):
		self.bot = Bot()

		Tkinter.Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.room_contents = Tkinter.StringVar()

		self.txtInput = Tkinter.Entry(self)
		self.txtInput["textvariable"] = self.room_contents
		self.txtInput.pack(side=Tkinter.TOP, fill=Tkinter.X, padx=2, pady=2)


		self.frmButtonFrame1 = Tkinter.Frame(self)
		self.frmButtonFrame1.pack(side=Tkinter.TOP, fill=Tkinter.X)

		self.btnQueNextGame = Tkinter.Button(self.frmButtonFrame1)
		self.btnQueNextGame["text"] = "Next"
		self.btnQueNextGame["command"] = self.startNextGame
		self.btnQueNextGame.pack(side=Tkinter.LEFT, padx=5, pady=5)

		self.btnRemovePlayer = Tkinter.Button(self.frmButtonFrame1)
		self.btnRemovePlayer["text"] = "Remove Selected"
		self.btnRemovePlayer["command"] = self.removeSelectedPlayer
		self.btnRemovePlayer.pack(side=Tkinter.RIGHT, padx=5, pady=5)


		self.frmButtonFrame2 = Tkinter.Frame(self)
		self.frmButtonFrame2.pack(side=Tkinter.TOP, fill=Tkinter.X)

		self.sclNumberOfPlayers = Tkinter.Scale(self.frmButtonFrame2, from_=1, to=8, orient=Tkinter.HORIZONTAL)
		self.sclNumberOfPlayers.pack(side=Tkinter.LEFT, padx=5, pady=5)

		self.btnBlacklistPlayer = Tkinter.Button(self.frmButtonFrame2)
		self.btnBlacklistPlayer["text"] = "Blacklist Selected"
		self.btnBlacklistPlayer["command"] = self.blacklistSelectedPlayer
		self.btnBlacklistPlayer.pack(side=Tkinter.RIGHT, padx=5, pady=5)


		self.lblLine = Tkinter.Label(self, text="LINE:", bg="black", fg="white", font=("Ariel Black", 16), anchor=Tkinter.W)
		self.lblLine.pack(side=Tkinter.TOP, fill=Tkinter.X, ipadx=0, ipady=0, padx=0, pady=0)

		self.lbxQueue = Tkinter.Listbox(self, borderwidth=0, bg="black", fg="white", font=("Ariel Black", 16), highlightthickness=0, relief="ridge")
		self.lbxQueue.pack(side=Tkinter.TOP, fill=Tkinter.BOTH, expand = 1, ipadx=0, ipady=0, padx=0, pady=0)
		self.lbxQueue.bind("<FocusOut>", self.unselectAll)

		self.lblInfo = Tkinter.Label(self, text="", anchor=Tkinter.W)
		self.lblInfo.pack(side=Tkinter.TOP, fill=Tkinter.X, ipadx=0, ipady=0, padx=0, pady=0)

		self.bot.add_queue_update_hook(self.update_queue_widget)

	def set_info(self, code, message):
		if code < 0:
			self.lblInfo.config(fg="darkred")
		elif code == 1:
			self.lblInfo.config(fg="darkblue")
		else:
			self.lblInfo.config(fg="black")
		self.lblInfo.config(text=message)

	def startNextGame(self):
		code, message = self.bot.startPlayers(self.room_contents.get(), self.sclNumberOfPlayers.get())
		self.set_info(code, message)

	def removeSelectedPlayer(self):
		selected_indexes = self.lbxQueue.curselection()
		if len(selected_indexes) > 0:
			index = selected_indexes[0]
			code, message = self.bot.remove_from_queue(index)
			self.set_info(code, message)
		else:
			self.set_info(-1, "No player was selected.")

	def blacklistSelectedPlayer(self):
		selected_indexes = self.lbxQueue.curselection()
		if len(selected_indexes) > 0:
			index = selected_indexes[0]
			code, message = self.bot.blacklist_player(index)
			self.set_info(code, message)
		else:
			self.set_info(-1, "No player was selected.")

	def unselectAll(self, event):
		print "lost focus"
		self.lbxQueue.selection_clear(0,Tkinter.END)

	def update_queue_widget(self, new_queue):
		self.lbxQueue.delete(0, Tkinter.END)
		for i in xrange(len(new_queue)):
			self.lbxQueue.insert(Tkinter.END, " "+str(i+1)+". "+str(new_queue[i]))


root = Tkinter.Tk()
app = Application(master=root)
app.pack(fill=Tkinter.BOTH, expand = 1)
app.mainloop()
root.destroy()

#TODO: Properly destroy the application when it's closed.