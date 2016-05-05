from bot import *
import time
import Tkinter


class Application(Tkinter.Frame):
	def createWidgets(self):
		self.room_contents = Tkinter.StringVar()

		self.txtInput = Tkinter.Entry(self)
		self.txtInput["textvariable"] = self.room_contents
		self.txtInput.pack(side=Tkinter.TOP, fill=Tkinter.X)

		self.btnQueNextGame = Tkinter.Button(self)
		self.btnQueNextGame["text"] = "Setup Next Player"
		self.btnQueNextGame["command"] = self.startNextGame
		self.btnQueNextGame.pack(side=Tkinter.TOP, fill=Tkinter.X)

		self.lbxQueue = Tkinter.Listbox(self, bg="black", fg="white", font=("Ariel Black", 16))
		self.lbxQueue.pack(side=Tkinter.TOP, fill=Tkinter.BOTH, expand=1)

		self.bot.add_queue_update_hook(self.update_queue_widget)

	def startNextGame(self):
		self.bot.startPlayers(self.room_contents.get())

	def update_queue_widget(self, new_queue):
		self.lbxQueue.delete(0, Tkinter.END)
		for i in xrange(len(new_queue)):
			self.lbxQueue.insert(Tkinter.END, str(i+1)+". "+str(new_queue[i]))

	def __init__(self, master=None):
		self.bot = Bot()
		Tkinter.Frame.__init__(self, master)
		self.pack()
		self.createWidgets()


root = Tkinter.Tk()
app = Application(master=root)
app.mainloop()
root.destroy()