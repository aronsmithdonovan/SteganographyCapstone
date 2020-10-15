import tkinter as tk
from encode import *
from tkinter import filedialog


class BasicGUI1:

    def __init__(self):
        """Create a BasicGUI1 object, setting up the GUI in the process"""

        # set up the overall window, as an instance variable
        self.rootWin = tk.Tk()
        self.rootWin.title("First example")

        # set up a label as a local variable (doesn't need to be accessed)
        titleLabel = tk.Label(self.rootWin, text="Welcome to my program!",
                              font="Arial 20 bold", relief=tk.GROOVE,
                              justify=tk.CENTER)
        titleLabel.grid(row=0, column=0, columnspan=3)

        #text
        entryText = tk.Entry(self.rootWin, text = "Please enter text",
                             font = "Arial 16")
        entryText.grid(row = 1, column = 1)
        self.text = entryText.get()
        #png file
        # browseButton = tk.Button(self.rootWin, text = "Browse png files", command = self.fileDialog)
        # browseButton.grid(row = 2, column = 0)

        #enter button
        enterButton = tk.Button(self.rootWin, text = "Enter", command= self.encode1)
        enterButton.grid(row =2, column =0)

        # set up a button as a local variable (doesn't need to be accessed)
        quitButton = tk.Button(self.rootWin, text="Quit",
                               font="Arial 16", command=self.quit)
        quitButton.grid(row=2, column=1)




    # This method just calls the root window's method for starting everything
    # running.  There are other ways in later examples for running the GUI
    def go(self):
        """This takes no inputs, and sets the GUI running"""
        self.rootWin.mainloop()



    def encode1(self):

        self.filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetype=
        (("png files", "*.png"), ("all files", "*.*")))
        main(self.text, self.filename)


    def quit(self):
        """This is a callback method attached to the quit button.
        It destroys the main window, which ends the program"""
        self.rootWin.destroy()


# --------------------------------
# Below here is the script part, which creates the object and sets it running
myGui = BasicGUI1()
myGui.go()
