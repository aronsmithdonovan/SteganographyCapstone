# stegGUI.py
# 
# handles GUI components
# 
# -------------------------------------------------------------------------------------------

# inputs
import tkinter as tk
from encodeLSB import *
from decodeLSB import *
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk
from PIL import Image
from pathlib import Path
import itertools
import pyperclip

# -------------------------------------------------------------------------------------------

# creates a BasicGUI object
class BasicGUI1:

    # initialization
    def __init__(self):

        # -------------------------------------------------------------------------------------------
        
        # set up the overall window (as an instance variable)
        self.rootWin = tk.Tk()
        self.rootWin.geometry("1000x650")
        self.rootWin.title("Steganography Encoder")
        
        # -------------------------------------------------------------------------------------------
        
        # choose color scheme (http://www.science.smith.edu/dftwiki/images/3/3d/TkInterColorCharts.png)
        self.ENCODE_COLOR = "LightSkyBlue1"
        self.DECODE_COLOR = "dark sea green"

        # -------------------------------------------------------------------------------------------
        # set up frames
        self.headerFrame = tk.Frame(master=self.rootWin,
                                width=750,
                                height=25,
                                bg="black",
                                relief=tk.FLAT)
        self.toggleFrame = tk.Frame(master=self.rootWin,
                                width=750,
                                height=25,
                                bg="black",
                                relief=tk.FLAT)
        self.messageFrame = tk.Frame(master=self.rootWin,
                                width=750,
                                height=25,
                                bg=self.ENCODE_COLOR,
                                relief=tk.GROOVE)
        self.keyFrame = tk.Frame(master=self.rootWin,
                                width=750,
                                height=25,
                                bg=self.ENCODE_COLOR,
                                relief=tk.GROOVE)
        self.buttonFrame = tk.Frame(master=self.rootWin,
                                width=750,
                                height=25,
                                bg="snow2",
                                relief=tk.RIDGE)
        self.paddingFrame = tk.Frame(master=self.rootWin,
                                width=750,
                                height=200,
                                bg=self.ENCODE_COLOR,
                                relief=tk.FLAT)
        
        # -------------------------------------------------------------------------------------------
        
        # title label for header
        self.titleLabel = tk.Label(self.headerFrame,
                                text="Steganography Encoder",
                                font="Arial 20 bold",
                                fg="white",
                                bg="black")
        self.titleLabel.pack()
        
        # -------------------------------------------------------------------------------------------
        
        # encode/decode toggle button
        self.ENCODE_STATE = "DECODING MODE"
        self.DECODE_STATE = "ENCODING MODE"
        self.toggleState = self.ENCODE_STATE
        self.toggleCycle = itertools.cycle([self.DECODE_STATE, self.ENCODE_STATE])
        self.toggleButton = tk.Button(self.toggleFrame,
                                        text=self.ENCODE_STATE,
                                        font="Arial 12",
                                        fg="black",
                                        bg=self.DECODE_COLOR,
                                        command=self.toggle)
        self.toggleButton.pack(fill=tk.Y, side=tk.LEFT)
        
        # -------------------------------------------------------------------------------------------
        
        # text input label
        self.inputTextLabel = tk.Label(self.messageFrame,
                                text="Enter message to be encoded:",
                                font="Arial 12",
                                fg="black",
                                bg=self.ENCODE_COLOR)
        self.inputTextLabel.pack(fill=tk.X, side=tk.LEFT)
        
        # text input object
        self.inputText = tk.Entry(self.messageFrame,
                                font = "Arial 12",
                                text="",
                                fg="black",
                                bg="white")
        self.inputText.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        # upload .txt file
        self.inputTextFileButton = tk.Button(self.messageFrame,
                                            text="Upload .txt file",
                                            font="Arial 12",
                                            fg="black",
                                            bg="white",
                                            command=self.textFileProcess)
        self.inputTextFileButton.pack(side=tk.LEFT)

        # get text input
        self.text = self.inputText.get()
        
        # -------------------------------------------------------------------------------------------
        
        # encryption key label
        self.keyLabel = tk.Label(self.keyFrame,
                                text="Encryption key:",
                                font="Arial 12",
                                fg="black",
                                bg=self.ENCODE_COLOR)
        self.keyLabel.pack(fill=tk.X, side=tk.LEFT)

        # encryption key return
        self.enc_key = ""
        self.keyReturn = tk.Label(self.keyFrame,
                                text="key will display here after your message is encoded",
                                font="Arial 12 italic",
                                fg="grey",
                                bg=self.ENCODE_COLOR)
        self.keyReturn.pack(fill=tk.X, side=tk.LEFT)

        # saves key to .txt file
        self.outputSaveButton = tk.Button(self.keyFrame,
                                        text="Save key to .txt file (recommended)",
                                        font="Arial 12",
                                        fg="black",
                                        bg="white")

        # -------------------------------------------------------------------------------------------
        
        # select image file button
        self.imgUploadButton = tk.Button(self.buttonFrame,
                                text="Upload image file",
                                font="Arial 12",
                                fg="black",
                                bg="white",
                                command= self.imageFileProcess)
        self.imgUploadButton.pack(fill=tk.X, side=tk.RIGHT)

        # image filepath label
        self.imgFileLabel = tk.Label(self.buttonFrame,
                                        text="",
                                        font="Arial 12",
                                        fg="black",
                                        bg="snow2")
        self.imgFileLabel.pack(fill=tk.X, side=tk.LEFT)

        # image box
        self.imageBox = tk.Label(self.paddingFrame,
                                    bg=self.ENCODE_COLOR,
                                    width=700,
                                    height=400,
                                    anchor=CENTER,
                                    text="")

        # process image button
        self.processImgButton = tk.Button(self.paddingFrame,
                                            text="ENCODE IMAGE",
                                            command=self.encode_img,
                                            font="Arial 12",
                                            fg="black",
                                            bg="white",
                                            width=50,
                                            height=1,)
        self.processImgButton.pack(side=tk.BOTTOM)

        # -------------------------------------------------------------------------------------------

        # quit button
        self.quitButton = tk.Button(self.toggleFrame,
                                text="Quit   X",
                                font="Arial 12 bold",
                                fg="black",
                                bg="tomato",
                                command=self.quit)
        self.quitButton.pack(fill=tk.X, side=tk.RIGHT)

        # -------------------------------------------------------------------------------------------
        
        # pack frames
        self.headerFrame.pack(fill=tk.X, side=tk.TOP)
        self.toggleFrame.pack(fill=tk.X, side=tk.TOP)
        self.messageFrame.pack(fill=tk.X, side=tk.TOP)
        self.keyFrame.pack(fill=tk.X, side=tk.TOP)
        self.buttonFrame.pack(fill=tk.X, side=tk.TOP)
        self.paddingFrame.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)
        
        # -------------------------------------------------------------------------------------------
    

    # -------------------------------------------------------------------------------------------
    
    # starts the GUI
    def go(self):
        self.rootWin.mainloop()

    # -------------------------------------------------------------------------------------------
    
    # toggle function to switch between encoding and decoding
    def toggle(self):
        self.toggleState = next(self.toggleCycle)
        self.toggleButton['text'] = str(self.toggleState)

        if self.toggleState == self.ENCODE_STATE: # IF IN ENCODING MODE:

            # config frames
            self.headerFrame.config(width=750,
                                    height=25,
                                    bg="black",
                                    relief=tk.FLAT)
            self.toggleFrame.config(width=750,
                                    height=25,
                                    bg="black",
                                    relief=tk.FLAT)
            self.messageFrame.config(width=750,
                                        height=25,
                                        bg=self.ENCODE_COLOR,
                                        relief=tk.GROOVE)
            self.keyFrame.config(width=750,
                                    height=25,
                                    bg=self.ENCODE_COLOR,
                                    relief=tk.GROOVE)
            self.buttonFrame.config(width=750,
                                    height=25,
                                    bg="snow2",
                                    relief=tk.RIDGE)
            self.paddingFrame.config(width=750,
                                        height=200,
                                        bg=self.ENCODE_COLOR,
                                        relief=tk.FLAT)
            
            # -------------------------------------------------------------------------------------------
            
            # config title label for header
            self.titleLabel.config(text="Steganography Encoder",
                                    font="Arial 20 bold",
                                    fg="white",
                                    bg="black")
            self.titleLabel.pack()
            
            # -------------------------------------------------------------------------------------------
            
            # config toggle button
            self.toggleButton.config(text=self.ENCODE_STATE,
                                        font="Arial 12",
                                        fg="black",
                                        bg=self.DECODE_COLOR,
                                        command=self.toggle)
            self.toggleButton.pack(fill=tk.Y, side=tk.LEFT)
            
            # -------------------------------------------------------------------------------------------
            
            # config text input label
            self.inputTextLabel.config(text="Enter message to be encoded:",
                                        font="Arial 12",
                                        fg="black",
                                        bg=self.ENCODE_COLOR)
            self.inputTextLabel.pack(fill=tk.X, side=tk.LEFT)
            
            # config text input object
            
            self.inputText.config(font = "Arial 12",
                                    text="",
                                    fg="black",
                                    bg="white")
            self.inputText.delete(0,END)
            self.inputText.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

            # config upload .txt file
            self.inputTextFileButton.config(text="Upload .txt file",
                                                font="Arial 12",
                                                fg="black",
                                                bg="white",
                                                command=self.textFileProcess)
            self.inputTextFileButton.pack(side=tk.LEFT)

            # get text input
            self.text = self.inputText.get()
            
            # -------------------------------------------------------------------------------------------
            
            # config encryption key label
            self.keyLabel.config(text="Encryption key:",
                                    font="Arial 12",
                                    fg="black",
                                    bg=self.ENCODE_COLOR)
            self.keyLabel.pack(fill=tk.X, side=tk.LEFT)

            # config encryption key return
            self.enc_key = ""
            self.keyReturn.config(text="key will display here after your message is encoded",
                                    font="Arial 12 italic",
                                    fg="grey",
                                    bg=self.ENCODE_COLOR)
            self.keyReturn.pack(fill=tk.X, side=tk.LEFT)

            # config save key to .txt file
            self.outputSaveButton.config(text="Save key as .txt file (recommended)",
                                        font="Arial 12",
                                        fg="black",
                                        bg="white")

            # -------------------------------------------------------------------------------------------
            
            # config select image file button
            self.imgUploadButton.config(text="Upload image file",
                                        font="Arial 12",
                                        fg="black",
                                        bg="white",
                                        command= self.imageFileProcess)
            self.imgUploadButton.pack(fill=tk.X, side=tk.RIGHT)

            # config image filepath label
            self.imgFileLabel.config(text="",
                                        font="Arial 12",
                                        fg="black",
                                        bg="snow2")
            self.imgFileLabel.pack(fill=tk.X, side=tk.LEFT)

            # config image box
            self.imageBox.config(bg=self.ENCODE_COLOR,
                                    text="",
                                    image='')

            # config process image button
            self.processImgButton.config(text="ENCODE IMAGE",
                                            command=self.encode_img,
                                            font="Arial 12",
                                            fg="black",
                                            bg="white",
                                            width=50,
                                            height=1,)
            self.processImgButton.pack(side=tk.BOTTOM)

            # -------------------------------------------------------------------------------------------

            # config quit button
            self.quitButton.config(text="Quit   X",
                                    font="Arial 12 bold",
                                    fg="black",
                                    bg="tomato",
                                    command=self.quit)
            self.quitButton.pack(fill=tk.X, side=tk.RIGHT)

            # -------------------------------------------------------------------------------------------
            
            # pack frames
            self.headerFrame.pack(fill=tk.X, side=tk.TOP)
            self.toggleFrame.pack(fill=tk.X, side=tk.TOP)
            self.messageFrame.pack(fill=tk.X, side=tk.TOP)
            self.keyFrame.pack(fill=tk.X, side=tk.TOP)
            self.buttonFrame.pack(fill=tk.X, side=tk.TOP)
            self.paddingFrame.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)
        
        elif self.toggleState == self.DECODE_STATE: # IF IN DECODING MODE:

            # config frames
            self.headerFrame.config(width=750,
                                    height=25,
                                    bg="black",
                                    relief=tk.FLAT)
            self.toggleFrame.config(width=750,
                                    height=25,
                                    bg="black",
                                    relief=tk.FLAT)
            self.messageFrame.config(width=750,
                                        height=25,
                                        bg=self.DECODE_COLOR,
                                        relief=tk.GROOVE)
            self.keyFrame.config(width=750,
                                    height=25,
                                    bg=self.DECODE_COLOR,
                                    relief=tk.GROOVE)
            self.buttonFrame.config(width=750,
                                    height=25,
                                    bg="snow2",
                                    relief=tk.RIDGE)
            self.paddingFrame.config(width=750,
                                        height=200,
                                        bg=self.DECODE_COLOR,
                                        relief=tk.FLAT)
            
            # -------------------------------------------------------------------------------------------
            
            # config title label for header
            self.titleLabel.config(text="Steganography Decoder",
                                    font="Arial 20 bold",
                                    fg="white",
                                    bg="black")
            self.titleLabel.pack()
            
            # -------------------------------------------------------------------------------------------
            
            # config toggle button
            self.toggleButton.config(text=self.DECODE_STATE,
                                        font="Arial 12",
                                        fg="black",
                                        bg=self.ENCODE_COLOR,
                                        command=self.toggle)
            self.toggleButton.pack(fill=tk.Y, side=tk.LEFT)
            
            # -------------------------------------------------------------------------------------------
            
            # config text input label
            self.inputTextLabel.config(text="Enter key to decode image:",
                                        font="Arial 12",
                                        fg="black",
                                        bg=self.DECODE_COLOR)
            self.inputTextLabel.pack(fill=tk.X, side=tk.LEFT)
            
            # config text input object
            self.inputText.config(font = "Arial 12",
                                    text="",
                                    fg="black",
                                    bg="white")
            self.inputText.delete(0,END)
            self.inputText.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

            # config upload .txt file
            self.inputTextFileButton.config(text="Upload .txt file",
                                                font="Arial 12",
                                                fg="black",
                                                bg="white",
                                                command=self.textFileProcess)
            self.inputTextFileButton.pack(side=tk.LEFT)

            # get text input
            self.text = self.inputText.get()
            
            # -------------------------------------------------------------------------------------------
            
            # config encryption key label
            self.keyLabel.config(text="Decoded message:",
                                    font="Arial 12",
                                    fg="black",
                                    bg=self.DECODE_COLOR)
            self.keyLabel.pack(fill=tk.X, side=tk.LEFT)

            # config encryption key return
            self.enc_key = ""
            self.keyReturn.config(text="message will display here after your image is decoded",
                                    font="Arial 12 italic",
                                    fg="grey",
                                    bg=self.DECODE_COLOR)
            self.keyReturn.pack(fill=tk.X, side=tk.LEFT)

            # config save message as .txt file
            self.outputSaveButton.config(text="Save message as .txt file",
                                        font="Arial 12",
                                        fg="black",
                                        bg="white")

            # -------------------------------------------------------------------------------------------
            
            # config select image file button
            self.imgUploadButton.config(text="Upload image file",
                                        font="Arial 12",
                                        fg="black",
                                        bg="white",
                                        command= self.imageFileProcess)
            self.imgUploadButton.pack(fill=tk.X, side=tk.RIGHT)

            # config image filepath label
            self.imgFileLabel.config(text="",
                                        font="Arial 12",
                                        fg="black",
                                        bg="snow2")
            self.imgFileLabel.pack(fill=tk.X, side=tk.LEFT)

            # config image box
            self.imageBox.config(bg=self.DECODE_COLOR,
                                    text="",
                                    image='')

            # config process image button
            self.processImgButton.config(text="DECODE MESSAGE",
                                            command=self.decode_img,
                                            font="Arial 12",
                                            fg="black",
                                            bg="white",
                                            width=50,
                                            height=1,)
            self.processImgButton.pack(side=tk.BOTTOM)

            # -------------------------------------------------------------------------------------------

            # config quit button
            self.quitButton.config(text="Quit   X",
                                    font="Arial 12 bold",
                                    fg="black",
                                    bg="tomato",
                                    command=self.quit)
            self.quitButton.pack(fill=tk.X, side=tk.RIGHT)

            # -------------------------------------------------------------------------------------------
            
            # pack frames
            self.headerFrame.pack(fill=tk.X, side=tk.TOP)
            self.toggleFrame.pack(fill=tk.X, side=tk.TOP)
            self.messageFrame.pack(fill=tk.X, side=tk.TOP)
            self.keyFrame.pack(fill=tk.X, side=tk.TOP)
            self.buttonFrame.pack(fill=tk.X, side=tk.TOP)
            self.paddingFrame.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)
        
        else:
            self.quit

    # -------------------------------------------------------------------------------------------

    # encodes image selected by user
    def encode_img(self):
        
        # get text
        self.text = self.inputText.get()

        # encode provided image with encrypted message 
        self.enc_image, self.enc_key = callEncode(self.text, self.filepath)

        # rename encoded image
        self.enc_filename = ('encoded_' + str(Path(self.filepath).name))
        
        # set filepath for encoded image to be in the same directory as the provided image
        self.enc_filepath = (str(Path(self.filepath).parent) + "\\" + str(self.enc_filename))
        
        # save the encoded image
        self.enc_image.save(self.enc_filepath)

        # display the filepath on the label
        self.imgFileLabel.config(text=self.enc_filepath)
        self.imgFileLabel.pack(fill=tk.X, side=tk.LEFT)

        # display the encoded image
        load = Image.open(self.enc_filepath)
        render = ImageTk.PhotoImage(load)
        self.imageBox.config(image=render)
        self.imageBox.image = render
        self.imageBox.pack()

        # display the encryption key
        self.keyReturn.config(text=str(self.enc_key), font="Arial 12 bold", fg="black") 
        self.keyReturn.pack(fill=tk.X, side=tk.LEFT)
        
        # update save button
        self.txt_filename=str(Path(self.filepath).stem + "_encryption-key.txt")
        self.txt_string=self.enc_key
        self.outputSaveButton.config(command=self.stringToTxt)
        self.outputSaveButton.pack(side=tk.RIGHT)

    # -------------------------------------------------------------------------------------------

    # decodes image selected by user
    def decode_img(self):

        # get text
        self.text = self.inputText.get()

        # decode provided image (text is key input)
        self.dec_msg = callDecode(self.filepath, self.text) 
        print(self.dec_msg)

        # display returned message
        self.keyReturn.config(text=str(self.dec_msg), font="Arial 12 bold", fg="black") 
        self.keyReturn.pack(fill=tk.X, side=tk.LEFT)
        
        # update save button
        self.txt_filename=str(Path(self.filepath).stem + "_decoded-message.txt")
        self.txt_string=self.dec_msg
        self.outputSaveButton.config(command=self.stringToTxt)
        self.outputSaveButton.pack(side=tk.RIGHT)

    # -------------------------------------------------------------------------------------------

    # gets .txt file as message input
    def textFileProcess(self):
        
        # get filepath from file explorer
        txtfilepath = filedialog.askopenfilename(initialdir="C:/", title="Select a text file", filetype=(("text files", "*.txt"), ("all files", "*.*")))
        
        # clear current input text
        self.inputText.delete(0,END)
        
        # set input text contents to the contents of the text file
        txtContents = str(open(txtfilepath, 'r').read())
        self.inputText.insert(0, txtContents)

        # display the filepath on the upload button
        self.inputTextFileButton.config(text=txtfilepath)
        self.inputTextFileButton.pack(side=tk.LEFT)

    # -------------------------------------------------------------------------------------------

    # gets image file as input
    def imageFileProcess(self):

        # get filepath from file explorer
        self.filepath = filedialog.askopenfilename(initialdir="C:/", title="Select an image file", filetype=(("png files", "*.png"), ("all files", "*.*")))

        # display the filepath on the label
        self.imgFileLabel.config(text=self.filepath)
        self.imgFileLabel.pack(fill=tk.X, side=tk.LEFT)

        # display the uploaded image
        load = Image.open(self.filepath)
        render = ImageTk.PhotoImage(load)
        self.imageBox.config(image=render)
        self.imageBox.image = render
        self.imageBox.pack()

    # -------------------------------------------------------------------------------------------

    # saves string as .txt file
    def stringToTxt(self):
        
        # set filepath for saved string to be in the same directory as the provided image
        self.txt_filepath = (str(Path(self.filepath).parent) + "\\" + self.txt_filename)

        # write text file
        file = open(self.txt_filepath, "x+")
        file.write(self.txt_string)
        file.close()

        # update button
        self.outputSaveButton.config(text="Saved!")

    # closes window and ends the program
    def quit(self):
        self.rootWin.destroy()

    # -------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------

# creates a GUI object and runs it
myGui = BasicGUI1()
myGui.go()
