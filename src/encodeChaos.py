# encodeChaos.py
#
# contains methods for encoding a message in an image
#
# -------------------------------------------------------------------------------------------

# imports
from PIL import Image
from numpy import *
from src.process import *
import cv2 as cv

# ------------------------------------------------------------------------------------------- ############### main()

# main
# uses command line, takes message input and encodes it in an image input
def main():
    # take message input
    print("\nEnter the message to encode:")

    # encrypt message
    encrypted_msg = EncryptedMessage(str(input()))

    # print key
    key = encrypted_msg.getKey()
    # print("\nYour generated key is:\n" + 
    #         key.decode('utf-8') + 
    #         "\n\nSave this key to be able to decrypt your message.")

    # take image input
    image_file = "cat.png"
    image = Image.open(image_file, 'r')

    # encode encrypted message in image
    enc_image, edge_key = encode(image, encrypted_msg.getBinList())

    # update key
    key = str(key.decode("utf-8") + "!" + edge_key)
    print("\nYour generated key is:\n" + 
            key + 
            "\n\nSave this key to be able to decrypt your message.")

    # save encoded image
    enc_image.save('encodedCat.png')

# ------------------------------------------------------------------------------------------- ############### callEncodeChaos(message, image_input)

# callEncodeChaos
### message: input message string
### image_input: filepath for image to be encoded
### return: encoded image
def callEncodeChaos(message, image_input):

    # encrypt message
    encrypted_msg = EncryptedMessage(str(message))

    # save key
    key = encrypted_msg.getKey()

    # encode encrypted message in image
    enc_image, edge_key = encode(image_input, encrypted_msg.getBinList())

    # update key
    key = str(key.decode("utf-8") + "!" + edge_key)

    # return statement
    return enc_image, key

# ------------------------------------------------------------------------------------------- ############### encode(image, data)

# encode
# encodes a list of binary values into the edge pixels of an image using Canny edge detection
# uses half as many pixels as LSB
### image: filepath for input image
### data: list of binary values to be encoded into an image
### return: encoded image
def encode(image_input, data):
    
    # take image input
    image_file = image_input
    image = Image.open(image_file, 'r')
    # image = Image.open('cat.png', 'r')

    # copies input image, convert to RGB
    enc_image = image.copy()
    enc_image = enc_image.convert('RGB')

    # initialize arguments
    msg = ''

    for byte in data:
        msg = msg + byte

    # mark the end of the msg with 16 zeros
    msg = msg + '0000000000000000'

    #determines number of pix necessary for encoding
    pixnum = int(len(msg)/2)

    #selects edge pix for encodeding, adds to list
    edges = cv.Canny(cv.imread(image_input, 0),100,200) # TODO: SHOULD BE IMAGE OR ENC_IMAGE AS PARAM -- Still need to resolve later
    # edges = cv.Canny(cv.imread('cat.png', 0),100,200)
    
    edge_pix = []
    for i in range(edges.shape[0]):
        for j in range(edges.shape[1]):
            if edges[i,j] != 0:
                edge_pix.append((i,j))
    
    edge_return = ""
    separator = ", "
    for i in range(0, pixnum):
        edge_return += str(edge_pix[i])[1:-1]
        if i != pixnum:
            edge_return += separator

    encrypted_edge = EncryptedMessage(edge_return)
    edge_key = encrypted_edge.getKey().decode("utf-8")
    edge_enc_msg = encrypted_edge.getString()
    edge_enc_return = str(edge_key + "!" + edge_enc_msg)

    # copies pixel data for input image
    pixels = enc_image.load()

    # initializes variables for loop
    k = 0

    for i in range(pixnum):
        # get RGB values for current edge pixel
        r, g, b = pixels[edge_pix[i][1], edge_pix[i][0]]

        # convert rgb into binary
        r_bit = bin(r)
        g_bit = bin(g)
        b_bit = bin(b)

        # encode as outlined in Roy et al paper
        a1 = int(r_bit[len(r_bit)-1])
        a2 = int(g_bit[len(g_bit)-1])
        a3 = int(b_bit[len(b_bit)-1])


        x1 = int(msg[k])
        x2 = int(msg[k + 1])

        if (x1 == (a1^a3)) & (x2 == (a2^a3)):
            pass
        elif (x1 == (a1^a3)) & (x2 != (a2^a3)):
            g_bit = g_bit[0 : len(g_bit) - 1] + str((a2 + 1)%2)
        elif (x1 != (a1^a3)) & (x2 == (a2^a3)):
            r_bit = r_bit[0 : len(r_bit) - 1] + str((a1 + 1)%2)
        elif (x1 != (a1^a3)) & (x2 != (a2^a3)):
            b_bit = b_bit[0 : len(b_bit) - 1] + str((a3 + 1)%2)
        else:
            print('ERROR')

        k = k+2

        # save updated pixel
        pixels[edge_pix[i][1], edge_pix[i][0]] = (int(r_bit, 2), int(g_bit, 2), int(b_bit, 2))

        # save pixel location

    return enc_image, edge_enc_return

# -------------------------------------------------------------------------------------------

# call main fxn
if __name__ == '__main__' :
    main()

# -------------------------------------------------------------------------------------------

# end of file