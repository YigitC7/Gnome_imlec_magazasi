# Developer: Yiğit Çıtak
# Github.com/YigitC7
# yigitcitak.1817@gmail.com
# TR

import customtkinter as ctk # is not tkinter :D
from os import path, mkdir

import img_create
import Widgets
import internet_uyari
import indirme_motoru

class mainWindow:
	def __init__(self,window):
		self.window = window
		self.window.title("Gnome İmleç Mağazası")
		self.window.geometry("1200x700")
		self.window.minsize(1200,700)
		self.window.maxsize(1920,1080)
		self.window.configure(fg_color="#436eee")

		if indirme_motoru.internet_var_mi() == True:
			Widgets.widget(self.window)
		else:
			internet_uyari.wid(self.window)

		#img_create.arka_plan_ekle(self.window,"IMG/Arka_plan1.png")

		
if __name__ == "__main__":
	try:
		mkdir(path.expanduser("~")+"/.icons")
	except:
		pass
	window = ctk.CTk()
	app = mainWindow(window)
	window.mainloop()