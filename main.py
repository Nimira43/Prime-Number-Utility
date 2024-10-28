import customtkinter as ctk
from settings import *
import tkintermapview

class App(ctk.CTk):
  def __init__(self):
    super().__init__()
    ctk.set_appearance_mode('light')
    self.geometry('1200x800+100+50')
    self.minsize(800,600)
    self.title('Map Viewer')
    self.iconbitmap('map.ico')
    self.rowconfigure(0, weight = 1, uniform = 'a')
    self.columnconfigure(0, weight = 2, uniform = 'a')
    self.columnconfigure(0, weight = 8, uniform = 'a')
    self.mainloop()

App()