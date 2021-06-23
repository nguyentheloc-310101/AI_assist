

import speech_recognition
#from gtts import gTTS
import tkinter as tk 
from tkinter import *
import win32clipboard

class GUI(Frame):
	def __init__(self,master=None):
		Frame.__init__(self, master)
		self.master.title("Nhập văn bản bằng giọng nói")
		self.grid()

		self.lb1 = Label(master, text="Chỉ có 3s thôi nói lẹ đi ")
		self.lb1.grid(column=0, row=0)

		self.output = Text(master, height = 5, width = 25, bg = "light cyan") 
		self.output.grid()

		def copy_button():
			copy = self.output.get("1.0","end-1c")
			win32clipboard.OpenClipboard()
			win32clipboard.EmptyClipboard()
			win32clipboard.SetClipboardText(copy, win32clipboard.CF_UNICODETEXT)
			win32clipboard.CloseClipboard()
			print("Sen: Hãy nhấn [Ctrl + V] để paste")

		def hamnghe():
			with speech_recognition.Microphone() as mic:
				print("Sen: tớ đang nghe nè")
				nghe.adjust_for_ambient_noise(mic) 
				audio = nghe.record(mic, duration=3)
				you = ""
			try:
				you = nghe.recognize_google(audio,language="vi-VI")
				print("Bạn: "+ you)
			except Exception as e :
				print("Sen: tới ko hiểu" + str (e))	
			return self.output.insert(INSERT, you)

		self.b = Button(master,text ="play", command = hamnghe)
		self.b.grid(column=1, row=0)
		self.b2 = Button(master,text ="copy", command = copy_button)
		self.b2.grid(column=1, row=2)

if __name__ == "__main__":
	you = ""
	nghe = speech_recognition.Recognizer()
	guiFrame = GUI()    
	guiFrame.mainloop()

