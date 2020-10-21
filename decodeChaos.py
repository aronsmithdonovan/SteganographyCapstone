# decodeLSB.py
#
# contains methods for decoding a message in an image
#
# -------------------------------------------------------------------------------------------

# imports
from PIL import Image
from process import *
import cv2 as cv

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

# ------------------------------------------------------------------------------------------- ############### callDecodeChaos(image_input, key)

# callDecodeChaos
# calls the decode function with internally provided message and image
### image_input: filepath for image to be decoded
### key: encryption key to decode image
### return: message string
def callDecodeChaos(image_input, key):

    # initialize arguments
    key = str(key)

    # decrypt message
    message = decode(image_input, key)

    # return statement
    return message

# ------------------------------------------------------------------------------------------- ############### decode(image, key)

# decode
# decodes a message encoded in an image using the encode function in encodeLSB.py
### image: image with encoded message
### key: key used to encode message
### returns: DecryptedMessage file
def decode(image_input, key):

    # split key inputs
    key_list = key.split("!")
    key = str(key_list[0])
    dcr_edge = DecryptedMessage(key_list[2], key_list[1]).getString()
    split_edge = dcr_edge.split(", ")
    split_edge.pop()
    for i in range(0, len(split_edge)):
        split_edge[i] = int(split_edge[i])
    edge_pix = list(zip(split_edge[::2],split_edge[1::2]))
    
    # take image input
    image = Image.open(image_input, 'r')

    # copies pixel data for input image
    image = image.convert('RGB')
    pixels = image.load()

    message = ''
    stop_decoding = False
    i = 0
    while(stop_decoding == False):
        # get RGB values for current edge pixel
        r, g, b = pixels[edge_pix[i][1], edge_pix[i][0]]


        # convert rgb into binary
        r_bit = bin(r)
        g_bit = bin(g)
        b_bit = bin(b)

        # decode as outlined in Roy et al. paper
        a1 = int(r_bit[len(r_bit) - 1])
        a2 = int(g_bit[len(g_bit) - 1])
        a3 = int(b_bit[len(b_bit) - 1])

        message = message + str(a1 ^ a3) + str(a2 ^ a3)

        i += 1



        # check for 16 zeros signifying end of message
        if len(message) >= 16:
            if (message[(len(message) - 16):(len(message))] == '0000000000000000') & (len(message)%8 == 0):
                stop_decoding = True

    # drop 16 zeros signifying end of msg
    message = message[0:(len(message) - 16)]

    # convert binary message to binary list
    bin_list = []
    for i in range(int(len(message)/8)):
        bin_list.append(message[8*i : 8*i + 8])


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