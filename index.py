from tkinter import ttk
from tkinter import *

import sqlite3

class Product:

    def __init__(self, window):
        # Initializations 
        self.wind = window
        self.wind.title('MARKETMASTER Application')

 
if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()
       