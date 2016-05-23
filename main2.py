from tkinter import *
from random import randint
from socket import *
from sys import * 
from threading import *


# Définition du port et de l'ip hote

HOST ='192.168.0.39'
PORT = 33000

class Reception (Thread) :
	''' Thread gérant la réception des messages '''
	def __init__ (self, conn) :
		Thread.__init__(self)
		self.connexion = conn

	def run (self) :
		while 1 :
			message_recu = self.connexion.recv(2048).decode("Utf8")
			if message_recu == "STOP" :
				break
		th_E._stop()
		etat = "connexion fermee"
		self.connexion.close()


class Emission (Thread) :
	'''Thread gérant l'émission des messages '''
	def __init__ (self, conn) :
		Thread.__init__(self)
		self.connexion = conn

	def run (self) :
		while 1 :
			message_envoye = message_entry
			self.connexion.send(message_envoye.encode("Utf8"))
		
		etat = "connexion fermee"
		self.connexion.close()
		sys.exit()



class Login(Tk):

	def __init__(self, boss=None):
	
		def idGenerator():
			id = StringVar()
			id.set(str(randint(10000000,99999999)))
			gen_lbl2.configure(textvariable=id)
			
		Tk.__init__(self)
		self.configure(width = 600, height = 450, bg = "black")
		self.title("CryptoChat")
		self.resizable(width = False, height = False)
		self.iconbitmap("ressource/logo.ico")
		
		connexion_lbl = Label(self, text = "Enter your ID to connect  :", bg="black", fg = "#2ee143")
		connexion_lbl.grid(row = 0, column = 0, padx = 5, pady = 5, ipadx = 2, ipady = 2, sticky = N)
		
		connexion_entry = Entry(self, bg = "black", fg = "#ff0000", relief = GROOVE, justify = CENTER, width = 18)
		connexion_entry.grid(row = 1, column = 0, padx = 5, pady = 5, ipadx = 2, ipady = 2, sticky = N)
		
		connexion_btn = Button(self, text = "CONNECT ME", command = Application, bg = "black", fg = "#2ee143", relief = GROOVE, justify = CENTER)
		connexion_btn.grid(row = 2, column = 0, padx = 5, pady = 5, ipadx = 2, ipady = 2, sticky = N)
		
		line_lbl = Label(self, text = "_______________________________________________", bg="black", fg = "#2ee143")
		line_lbl.grid(row = 3, column = 0, padx = 1, pady = 1, sticky = N)

		gen_lbl = Label(self, text = "Generate new ID  :", bg="black", fg = "#2ee143")
		gen_lbl.grid(row = 4, column = 0, padx = 5, pady = 5, ipadx = 2, ipady = 2, sticky = N)	

		gen_lbl2 = Label(self, textvariable = "", bg = "black", fg = "#ff0000", relief = FLAT, width = 10)
		gen_lbl2.grid(row = 5, column = 0, padx = 5, pady = 5, ipadx = 2, ipady = 2, sticky = N)

		gen_btn = Button(self, text = "GENERATE", command = idGenerator, bg = "black", fg = "#2ee143", relief = GROOVE)
		gen_btn.grid(row = 6, column = 0, padx = 5, pady = 5, ipadx = 2, ipady = 2, sticky = N)

class Application(Tk):

	def __init__(self, boss=None):
		etat = "connexion"
		Tk.__init__(self)
		root.destroy()
		self.configure(width = 600, height = 450, bg = "black")
		self.title("CryptoChat")
		self.resizable(width = False, height = False)
		self.iconbitmap("ressource/logo.ico")
		
		buddyId_lbl = Label(self, text = "Buddy ID  : ", bg="black", fg = "#2ee143")
		buddyId_lbl.grid(row = 0, column = 0, padx = 5, pady = 5, ipadx = 2, ipady = 2, sticky = N)
		
		buddyId_entry = Entry(self, bg = "black", fg = "#ff0000", relief = GROOVE, justify = CENTER, width = 18)
		buddyId_entry.grid(row = 0, column = 1, padx = 5, pady = 5, ipadx = 2, ipady = 2, sticky = N)
		
		buddyId_OK_btn = Button(self, text = "OK", command = "", bg = "black", fg = "#2ee143", relief = GROOVE, justify = CENTER)
		buddyId_OK_btn.grid(row = 0, column = 2, padx = 5, pady = 5, ipadx = 2, ipady = 2, sticky = N)
		
		status_lbl = Label(self, text = etat , bg= "black", fg = "#ffff00")
		status_lbl.grid(row = 0, column = 3, padx = 25, pady = 5, ipadx = 2, ipady = 2, sticky = E)
	
		messages_canvas = Canvas(self, width = 520, height = 390, bg = "#000000", relief = GROOVE,)
		messages_canvas.grid(row = 1, column = 0, columnspan = 4)
		
		message_entry = Entry(self, bg = "#000000", fg = "#0000ff", width = 86, relief = GROOVE, borderwidth = 2)
		message_entry.grid(row = 2, column = 0, columnspan = 4, padx = 5, pady = 5, ipadx = 2, ipady = 2)
		message_entry.get()
		

	def affichermessage (self) :
		
# Programme main


if __name__=='__main__':
	root = Login()
	root.mainloop()

connexion = socket(AF_INET, SOCK_STREAM)
try :
	connexion.connect((HOST, PORT))
except error :
	sys.exit()
	
etat = "connexion etablie"


th_E = Emission(connexion)
th_R = Reception(connexion)
th_E.start()
th_R.start()		
		

