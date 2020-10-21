# decodeLSB.py
#
# contains methods for decoding a message in an image
#
# -------------------------------------------------------------------------------------------

# imports
from PIL import Image
from process import *
import cv2 as cv

# -------------------------------------------------------------------------------------------





# main
def main():
    # take key input
    print("\nProvide the key used to encrypt the message:")
    key = str(input())

    # take image input
    # print("Enter the name of the image file (include extension)")
    # image_file = input()
    image_file = "encodedCat.png"
    image = Image.open(image_file, 'r')

    # decode message from image with key
    message = decode(image, key)

    # print decoded message
    print("\nYour decoded message is: " + message)


# -------------------------------------------------------------------------------------------

# decode
# decodes a message encoded in an image using the encode function in encodeLSB.py
### image: image with encoded message
### key: key used to encode message
### returns: DecryptedMessage file
def decode(image, key):

    # copies pixel data for input image
    image = image.convert('RGB')
    pixels = image.load()

    edges = cv.Canny(cv.imread('cat.png', 0), 100, 200)  # SHOULD BE IMAGE OR ENC_IMAGE AS PARAM -- still need to resolve later

    edge_pix = []

    for i in range(edges.shape[0]):
        for j in range(edges.shape[1]):
            if edges[i, j] != 0:
                edge_pix.append((i, j))



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

    #print(bin_list)

    # decrypt message
    message = DecryptedMessage(bin_list, key)
    # print(message.getString)


    # return message
    return message.getString()

# -------------------------------------------------------------------------------------------

# call main fxn
if __name__ == '__main__' :
    main()