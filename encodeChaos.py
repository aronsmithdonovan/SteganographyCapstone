# encodeChaos.py
#
# contains methods for encoding a message in an image
#
# -------------------------------------------------------------------------------------------

# imports
from PIL import Image
from numpy import *
from process import *
import cv2 as cv

# -------------------------------------------------------------------------------------------

# converts string to a list of binary
def stringToBinaryList(string):
    binary_string = ' '.join(format(ord(i), 'b') for i in string)
    binary_list = binary_string.split()
    binary_char_list = appendZeroes(binary_list)
    return binary_char_list

# -------------------------------------------------------------------------------------------

# main
# uses command line, takes message input and encodes it in an image input
def main():
    # take message input
    print("\nEnter the message to encode:")

    # encrypt message
    encrypted_msg = EncryptedMessage(str(input()))

    # print key
    key = encrypted_msg.getKey()
    print("\nYour generated key is:\n" + key.decode('utf-8') + "\n\nSave this key to be able to decrypt your message.")

    # take image input
    # print("Enter the name of the image file (include extension)")
    # image_file = input()
    image_file = "cat.png"
    image = Image.open(image_file, 'r')

    # encode encrypted message in image
    enc_image = encodeChaos(image, encrypted_msg.getBinList())

    # save encoded image
    enc_image.save('encodedCat.png')

    # display encoded image
    enc_image.show()


# -------------------------------------------------------------------------------------------

# encodeChaos
# encodes a list of binary values into the edge pixels of an image using Canny edge detection
# uses half as many pixels as LSB
### image: image object

def encodeChaos(image, data):
    # copies input image, convert to RGB
    enc_image = image.copy()
    enc_image = enc_image.convert('RGB')

    msg = data
    data = ''

    for byte in msg:
        data = data + byte

    # mark the end of the msg with 16 zeros
    data = data + '0000000000000000'

    #determines number of pix necessary for encoding
    pixnum = int(len(data)/2)

    #selects edge pix for encodeding, adds to list
    edges = cv.Canny(cv.imread('cat.png',0),100,200) #SHOULD BE IMAGE OR ENC_IMAGE AS PARAM -- Still need to resolve later
    edge_pix = []
    for i in range(edges.shape[0]):
        for j in range(edges.shape[1]):
            if edges[i,j] != 0:
                edge_pix.append((i,j))


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


        x1 = int(data[k])
        x2 = int(data[k + 1])

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

    return enc_image

# -------------------------------------------------------------------------------------------

# call main fxn
if __name__ == '__main__' :
    main()





