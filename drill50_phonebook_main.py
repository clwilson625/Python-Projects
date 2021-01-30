# Python Ver:           3.9
#
# Author:               Carol Wilson
#
# Purpose:              Phonebook Demo.  Demonstrating OOP, Tkinter GUI module,
#                            using Tkinter Parent and Child relationships.
#
# Tested OS:          This code was written and tested to work with Windows 10.

from tkinter import *
import tkinter as tk

# Be sure to import out other modules
# we need access to them for everything to work correctly
import drill50_phonebook_gui
import drill50_phonebook_func

# Frame is the Tkinter frame class that our own class will inherit from
# This section is defining a class and mountin a frame - primary Tkinter

class ParentWindow(Frame):
      def __init__(self, master, *args, **kwargs):
            Frame.__init__(self, master, *args, **kwargs)

            # This section will define out master frame configuration - incuding the address
            # to get it from and the size

            self.master = master
            self.master.minsize(500,300) #This is the height and width in pixels
            self.master.maxsize(500,300) # You will not the size is fixed
            # This CenterWindow method will center our app on the user's screen
            phonebook_func.center_window(self, 500,300)
            # This is the title
            self.master.title("The Tkinter Phonebook Demo")
            # This is the background color
            self.master.configure(bg="#F0F0F0")
            # This protocol method is a tkinter built-in method to catch if
            # the user clicks the upper corner, "X" on Windows OS.
            self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
            arg = self.master

            # load in the GUI widgets from a seperate module,
            # keeping your code comparmentalized and clutter free
            phonebook_gui.load_gui(self)




if __name__ == "__main__":
      root = tk.Tk()
      App = ParentWindow(root)
      root.mainloop()












            

            
