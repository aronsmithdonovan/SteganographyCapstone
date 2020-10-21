# stegGUI.py
# 
# handles GUI components
# 
# -------------------------------------------------------------------------------------------

# inputs
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from encodeLSB import *
from decodeLSB import *
from encodeChaos import *
from decodeChaos import *
from PIL import ImageTk
from PIL import Image
from pathlib import Path
import itertools

# ------------------------------------------------------------------------------------------- ############### GUI

# creates a GUI object
class GUI:

    # ------------------------------------------------------------------------------------------- ############### __init__(self)

    # initialization
    def __init__(self):

        # -------------------------------------------------------------------------------------------
        
        # set up the overall window (as an instance variable)
        self.rootWin = tk.Tk()
        self.rootWin.geometry("1000x650")
        self.rootWin.title("Steganography Application")
        
        # -------------------------------------------------------------------------------------------
        
        # choose color scheme (http://www.science.smith.edu/dftwiki/images/3/3d/TkInterColorCharts.png)
        self.ENCODE_COLOR = "LightSkyBlue1"
        self.DECODE_COLOR = "DarkSeaGreen3"
        self.LSB_COLOR = "goldenrod1"
        self.CHAOS_COLOR = "LightPink1"

        # -------------------------------------------------------------------------------------------
        
        # set up frames
        self.headerFrame = tk.Frame(master=self.rootWin,
                                width=750,
                                height=25,
                                bg="black",
                                relief=tk.FLAT)
        self.toggleProcessFrame = tk.Frame(master=self.rootWin,
                                width=750,
                                height=25,
                                bg="black",
                                relief=tk.FLAT)
        self.toggleMethodFrame = tk.Frame(master=self.rootWin,
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
        self.ENCODE_STATE = "MODE: Encoding"
        self.DECODE_STATE = "MODE: Decoding"
        self.toggleProcessState = self.ENCODE_STATE
        self.toggleProcessCycle = itertools.cycle([self.DECODE_STATE, self.ENCODE_STATE])
        self.toggleProcessButton = tk.Button(self.toggleProcessFrame,
                                        text="Change mode",
                                        font="Arial 12",
                                        fg="black",
                                        bg="white",
                                        command=self.toggleProcess)
        self.toggleProcessButton.pack(fill=tk.Y, side=tk.LEFT)

        # encode/decode toggle label
        self.toggleProcessLabel = tk.Label(self.toggleProcessFrame,
                                            text=self.ENCODE_STATE,
                                            font="Arial 12",
                                            fg="black",
                                            bg=self.DECODE_COLOR)
        self.toggleProcessLabel.pack(fill=tk.Y, side=tk.LEFT)

        # LSB/chaos toggle button
        self.LSB_STATE = "METHOD: Least Significant Bits"
        self.CHAOS_STATE = "METHOD: Scattered Bits"
        self.toggleMethodState = self.LSB_STATE
        self.toggleMethodCycle = itertools.cycle([self.CHAOS_STATE, self.LSB_STATE])
        self.toggleMethodButton = tk.Button(self.toggleMethodFrame,
                                        text="Change method",
                                        font="Arial 12",
                                        fg="black",
                                        bg="white",
                                        command=self.toggleMethod)
        self.toggleMethodButton.pack(fill=tk.Y, side=tk.LEFT)

        # LEB/chaos toggle label
        self.toggleMethodLabel = tk.Label(self.toggleMethodFrame,
                                            text=self.LSB_STATE,
                                            font="Arial 12",
                                            fg="black",
                                            bg=self.LSB_COLOR)
        self.toggleMethodLabel.pack(fill=tk.Y, side=tk.LEFT)
        
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
        self.quitButton = tk.Button(self.toggleProcessFrame,
                                text="Quit   X",
                                font="Arial 12 bold",
                                fg="black",
                                bg="tomato",
                                command=self.quit)
        self.quitButton.pack(fill=tk.X, side=tk.RIGHT)

        # -------------------------------------------------------------------------------------------
        
        # pack frames
        self.headerFrame.pack(fill=tk.X, side=tk.TOP)
        self.toggleProcessFrame.pack(fill=tk.X, side=tk.TOP)
        self.toggleMethodFrame.pack(fill=tk.X, side=tk.TOP)
        self.messageFrame.pack(fill=tk.X, side=tk.TOP)
        self.keyFrame.pack(fill=tk.X, side=tk.TOP)
        self.buttonFrame.pack(fill=tk.X, side=tk.TOP)
        self.paddingFrame.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)
        
        # -------------------------------------------------------------------------------------------
    

    # ------------------------------------------------------------------------------------------- ############### go(self)
    
    # starts the GUI
    def go(self):
        self.rootWin.mainloop()

    # ------------------------------------------------------------------------------------------- ############### toggleProcess(self)
    
    # toggle function to switch between encoding and decoding
    def toggleProcess(self):
        self.toggleProcessState = next(self.toggleProcessCycle)

        if self.toggleProcessState == self.ENCODE_STATE: ######################################### IF IN ENCODING MODE:

            # config frames
            self.messageFrame.config(bg=self.ENCODE_COLOR)
            self.keyFrame.config(bg=self.ENCODE_COLOR)
            self.paddingFrame.config(bg=self.ENCODE_COLOR)
            
            # -------------------------------------------------------------------------------------------
            
            # config title label for header
            self.titleLabel.config(text="Steganography Encoder")
            self.titleLabel.pack()
            
            # -------------------------------------------------------------------------------------------
            
            # config process toggle button
            self.toggleProcessButton.pack(fill=tk.Y, side=tk.LEFT)

            # config process toggle label
            self.toggleProcessLabel.config(text=self.ENCODE_STATE, bg=self.DECODE_COLOR)
            self.toggleProcessLabel.pack(fill=tk.Y, side=tk.LEFT)
            
            # -------------------------------------------------------------------------------------------
            
            # config text input label
            self.inputTextLabel.config(text="Enter message to be encoded:", bg=self.ENCODE_COLOR)
            self.inputTextLabel.pack(fill=tk.X, side=tk.LEFT)
            
            # config text input object
            self.inputText.config(text="")
            self.inputText.delete(0,END)
            self.inputText.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

            # config upload .txt file
            self.inputTextFileButton.config(text="Upload .txt file")
            self.inputTextFileButton.pack(side=tk.LEFT)
            
            # -------------------------------------------------------------------------------------------
            
            # config encryption key label
            self.keyLabel.config(text="Encryption key:", bg=self.ENCODE_COLOR)
            self.keyLabel.pack(fill=tk.X, side=tk.LEFT)

            # config encryption key return
            self.enc_key = ""
            self.keyReturn.config(text="key will display here after your message is encoded",
                                    font="Arial 12 italic",
                                    fg="grey",
                                    bg=self.ENCODE_COLOR)
            self.keyReturn.pack(fill=tk.X, side=tk.LEFT)

            # config save key to .txt file
            self.outputSaveButton.config(text="Save key as .txt file (recommended)")

            # -------------------------------------------------------------------------------------------
            
            # config select image file button
            self.imgUploadButton.pack(fill=tk.X, side=tk.RIGHT)

            # config image filepath label
            self.imgFileLabel.config(text="")
            self.imgFileLabel.pack(fill=tk.X, side=tk.LEFT)

            # config image box
            self.imageBox.config(bg=self.ENCODE_COLOR,
                                    text="",
                                    image='')

            # config process image button
            self.processImgButton.config(text="ENCODE IMAGE", command=self.encode_img)
            self.processImgButton.pack(side=tk.BOTTOM)

            # -------------------------------------------------------------------------------------------

            # config quit button
            self.quitButton.pack(fill=tk.X, side=tk.RIGHT)

            # -------------------------------------------------------------------------------------------
            
            # pack configurated frames
            self.headerFrame.pack(fill=tk.X, side=tk.TOP)
            self.toggleProcessFrame.pack(fill=tk.X, side=tk.TOP)
            self.toggleMethodFrame.pack(fill=tk.X, side=tk.TOP)
            self.messageFrame.pack(fill=tk.X, side=tk.TOP)
            self.keyFrame.pack(fill=tk.X, side=tk.TOP)
            self.buttonFrame.pack(fill=tk.X, side=tk.TOP)
            self.paddingFrame.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)
        
        elif self.toggleProcessState == self.DECODE_STATE: ######################################### IF IN DECODING MODE:

            # config frames
            self.messageFrame.config(bg=self.DECODE_COLOR)
            self.keyFrame.config(bg=self.DECODE_COLOR)
            self.paddingFrame.config(bg=self.DECODE_COLOR)
            
            # -------------------------------------------------------------------------------------------
            
            # config title label for header
            self.titleLabel.config(text="Steganography Decoder")
            self.titleLabel.pack()
            
            # -------------------------------------------------------------------------------------------
            
            # config process toggle label
            self.toggleProcessLabel.config(text=self.DECODE_STATE, bg=self.ENCODE_COLOR)
            self.toggleProcessLabel.pack(fill=tk.Y, side=tk.LEFT)
            
            # -------------------------------------------------------------------------------------------
            
            # config text input label
            self.inputTextLabel.config(text="Enter key to decode image:", bg=self.DECODE_COLOR)
            self.inputTextLabel.pack(fill=tk.X, side=tk.LEFT)
            
            # config text input object
            self.inputText.config(text="")
            self.inputText.delete(0,END)
            self.inputText.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

            # config upload .txt file
            self.inputTextFileButton.config(text="Upload .txt file")
            self.inputTextFileButton.pack(side=tk.LEFT)
            
            # -------------------------------------------------------------------------------------------
            
            # config encryption key label
            self.keyLabel.config(text="Decoded message:", bg=self.DECODE_COLOR)
            self.keyLabel.pack(fill=tk.X, side=tk.LEFT)

            # config encryption key return
            self.enc_key = ""
            self.keyReturn.config(text="message will display here after your image is decoded",
                                    font="Arial 12 italic",
                                    fg="grey",
                                    bg=self.DECODE_COLOR)
            self.keyReturn.pack(fill=tk.X, side=tk.LEFT)

            # config save message as .txt file
            self.outputSaveButton.config(text="Save message as .txt file")

            # -------------------------------------------------------------------------------------------
            
            # config select image file button
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
            self.toggleProcessFrame.pack(fill=tk.X, side=tk.TOP)
            self.toggleMethodFrame.pack(fill=tk.X, side=tk.TOP)
            self.messageFrame.pack(fill=tk.X, side=tk.TOP)
            self.keyFrame.pack(fill=tk.X, side=tk.TOP)
            self.buttonFrame.pack(fill=tk.X, side=tk.TOP)
            self.paddingFrame.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)
        
        else:
            self.quit

    # ------------------------------------------------------------------------------------------- ############### toggleMethod(self)
    
    # toggle function to switch between LSB and scatter methods
    def toggleMethod(self):
        self.toggleMethodState = next(self.toggleMethodCycle)

        if self.toggleMethodState == self.LSB_STATE: ######################################### IF IN LSB MODE...
            
            # config method toggle button
            self.toggleMethodButton.pack(fill=tk.Y, side=tk.LEFT)

            # config method toggle label
            self.toggleMethodLabel.config(text=self.LSB_STATE, bg=self.LSB_COLOR)
            self.toggleMethodLabel.pack(fill=tk.Y, side=tk.LEFT)

        elif self.toggleMethodState == self.CHAOS_STATE: ######################################### IF IN CHAOS MODE...
            
            # config method toggle button
            self.toggleMethodButton.pack(fill=tk.Y, side=tk.LEFT)

            # config method toggle label
            self.toggleMethodLabel.config(text=self.CHAOS_STATE, bg=self.CHAOS_COLOR)
            self.toggleMethodLabel.pack(fill=tk.Y, side=tk.LEFT)

        else:
            self.quit

    # ------------------------------------------------------------------------------------------- ############### encode_img(self)
    
    # encodes image selected by user
    def encode_img(self):
        
        # get text
        self.text = self.inputText.get()

        # encode provided image with encrypted message
        if self.toggleMethodState == self.LSB_STATE:
            self.enc_image, self.enc_key = callEncodeLSB(self.text, self.filepath)
        elif self.toggleMethodState == self.CHAOS_STATE:
            self.enc_image, self.enc_key = callEncodeChaos(self.text, self.filepath)
        else:
            self.quit

        # rename encoded image
        self.enc_filename = ('encoded_' + str(Path(self.filepath).name))
        
        # set filepath for encoded image to be in the same directory as the provided image
        self.enc_filepath = (str(Path(self.filepath).parent) + 
                                "\\" + str(self.enc_filename))
        
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

    # ------------------------------------------------------------------------------------------- ############### decode_img(self)

    # decodes image selected by user
    def decode_img(self):

        # get text
        self.text = self.inputText.get()

        # decode provided image (text is key input)
        if self.toggleMethodState == self.LSB_STATE:
            self.enc_image, self.enc_key = callDecodeLSB(self.filepath, self.text)
        elif self.toggleMethodState == self.CHAOS_STATE:
            self.enc_image, self.enc_key = callDecodeChaos(self.filepath, self.text)
        else:
            self.quit

        # display returned message
        self.keyReturn.config(text=str(self.dec_msg), font="Arial 12 bold", fg="black") 
        self.keyReturn.pack(fill=tk.X, side=tk.LEFT)
        
        # update save button
        self.txt_filename=str(Path(self.filepath).stem + "_decoded-message.txt")
        self.txt_string=self.dec_msg
        self.outputSaveButton.config(command=self.stringToTxt)
        self.outputSaveButton.pack(side=tk.RIGHT)

    # ------------------------------------------------------------------------------------------- ############### textFileProcess(self)

    # gets .txt file as message input
    def textFileProcess(self):
        
        # get filepath from file explorer
        txtfilepath = filedialog.askopenfilename(initialdir="C:/",
                                                    title="Select a text file",
                                                    filetype=(("text files", "*.txt"),
                                                    ("all files", "*.*")))
        
        # clear current input text
        self.inputText.delete(0,END)
        
        # set input text contents to the contents of the text file
        txtContents = str(open(txtfilepath, 'r').read())
        self.inputText.insert(0, txtContents)

        # display the filepath on the upload button
        self.inputTextFileButton.config(text=txtfilepath)
        self.inputTextFileButton.pack(side=tk.LEFT)

    # ------------------------------------------------------------------------------------------- ############### imageFileProcess(self)

    # gets image file as input
    def imageFileProcess(self):

        # get filepath from file explorer
        self.filepath = filedialog.askopenfilename(initialdir="C:/",
                                                    title="Select an image file",
                                                    filetype=(("png files", "*.png"),
                                                    ("all files", "*.*")))

        # display the filepath on the label
        self.imgFileLabel.config(text=self.filepath)
        self.imgFileLabel.pack(fill=tk.X, side=tk.LEFT)

        # display the uploaded image
        load = Image.open(self.filepath)
        render = ImageTk.PhotoImage(load)
        self.imageBox.config(image=render)
        self.imageBox.image = render
        self.imageBox.pack()

    # ------------------------------------------------------------------------------------------- ############### stringToTxt(self)

    # saves string as .txt file
    def stringToTxt(self):
        
        # set filepath for saved string to be in the same directory as the provided image
        self.txt_filepath = (str(Path(self.filepath).parent) + 
                                "\\" + self.txt_filename)

        # write text file
        file = open(self.txt_filepath, "x+")
        file.write(self.txt_string)
        file.close()

        # update button
        self.outputSaveButton.config(text="Saved!")

    # ------------------------------------------------------------------------------------------- ############### quit(self)

    # closes window and ends the program
    def quit(self):
        self.rootWin.destroy()

    # -------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------

# creates a GUI object and runs it
myGui = GUI()
myGui.go()

# -------------------------------------------------------------------------------------------

# end of file