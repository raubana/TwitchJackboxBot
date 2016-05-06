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

		self.frmButtonFrame = Tkinter.Frame(self)
		self.frmButtonFrame.pack(side=Tkinter.TOP, fill=Tkinter.X)

		self.btnQueNextGame = Tkinter.Button(self.frmButtonFrame)
		self.btnQueNextGame["text"] = "Next"
		self.btnQueNextGame["command"] = self.startNextGame
		self.btnQueNextGame.pack(side=Tkinter.LEFT, padx=10, pady=10)

		self.btnRemovePlayer = Tkinter.Button(self.frmButtonFrame)
		self.btnRemovePlayer["text"] = "Remove Selected"
		self.btnRemovePlayer["command"] = self.removeSelectedPlayer
		self.btnRemovePlayer.pack(side=Tkinter.RIGHT, padx=10, pady=10)

		self.lblLine = Tkinter.Label(self, text="LINE:", bg="black", fg="white", font=("Ariel Black", 16), anchor=Tkinter.W)
		self.lblLine.pack(side=Tkinter.TOP, fill=Tkinter.X, ipadx=0, ipady=0, padx=0, pady=0)

		self.lbxQueue = Tkinter.Listbox(self, borderwidth=0, bg="black", fg="white", font=("Ariel Black", 16), highlightthickness=0, relief="ridge")
		self.lbxQueue.pack(side=Tkinter.TOP, fill=Tkinter.BOTH, expand = 1, ipadx=0, ipady=0, padx=0, pady=0)
		self.lbxQueue.bind("<FocusOut>", self.unselectAll)

		self.bot.add_queue_update_hook(self.update_queue_widget)

	def startNextGame(self):
		self.bot.startPlayers(self.room_contents.get())

	def removeSelectedPlayer(self):
		selected_indexes = self.lbxQueue.curselection()
		if len(selected_indexes) > 0:
			index = selected_indexes[0]
			self.bot.remove_from_queue(index)

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