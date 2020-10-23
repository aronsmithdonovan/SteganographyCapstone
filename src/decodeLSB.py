# decodeLSB.py
# 
# contains methods for decoding a message in an image
# 
# -------------------------------------------------------------------------------------------

# imports
from PIL import Image
from src.process import *

# ------------------------------------------------------------------------------------------- ############### main()

# main
def main():
    
    # take key input
    print("\nProvide the key used to encrypt the message:")
    key = str(input())

    # get image
    image_file = "encodedCat.png"
    image = Image.open(image_file, 'r')

    # decode message from image with key
    message = decode(image, key)

    # print decoded message
    print("\nYour decoded message is: " + message)

# ------------------------------------------------------------------------------------------- ############### callDecodeLSB(image_input, key)

# callDecodeLSB
# calls the encode function with internally provided message and image
### image_input: filepath for image to be decoded
### key: encryption key to decode image
### return: message string
def callDecodeLSB(image_input, key):
    
    # initialize arguments
    key = str(key)
    image = Image.open(image_input, 'r')

    # decrypt message
    message = decode(image, key)

    # return statement
    return message

# ------------------------------------------------------------------------------------------- ############### decode(image, key)

# decode
# decodes a message encoded in an image using the encode function in encodeLSB.py
### image: image with encoded message
### key: key used to encode message
### returns: DecryptedMessage file
def decode(image, key):

    # copies pixel data for input image
    pixels = image.load()
    
    # initializes objects for zero counter
    zero_stack = []
    all_zeroes = "000000000"

    # sets width and height values
    width, height = image.size

    # initializes variables for loop
    w_index = 0
    h_index = 0
    bit_index = 0
    bin_string = ""
    bin_list = []
    not_zero = True

    while not_zero == True:
    
        # empty bin_string
        bin_string = ""

        # iterates through 3 pixels, gets least significant bit of RGB binary values
        for count in range(3):
            # get RGB values for current pixel
            r, g, b = pixels[w_index, h_index]

            # get least significant bit of each byte
            bin_string += bin(r)[-1]
            bin_string += bin(g)[-1]
            if count < 2:
                bin_string += bin(b)[-1]

            # update w_index
            if w_index == (width - 1):
                w_index = 0
                h_index += 1
            else:
                w_index += 1
        
        # check for zeroes
        if int(bin_string, 2) == 0:
            not_zero == False
            break
        
        # save string value
        bin_list.append(bin_string)

    # decrypt message
    message = DecryptedMessage(bin_list, key)

    # return message
    return message.getString()

# -------------------------------------------------------------------------------------------

# call main fxn
if __name__ == '__main__' :
    main()

# -------------------------------------------------------------------------------------------

# end of file