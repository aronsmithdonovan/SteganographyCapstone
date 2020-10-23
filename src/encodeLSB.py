# encodeLSB.py
# 
# contains methods for encoding a message in an image
# 
# -------------------------------------------------------------------------------------------

# imports
from PIL import Image
from src.process import *

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
    print("\nYour generated key is:\n" + 
            key.decode('utf-8') + 
            "\n\nSave this key to be able to decrypt your message.")
            
    # get image
    image_file = "cat.png"
    image = Image.open(image_file, 'r')

    # encode encrypted message in image
    enc_image = encode(image, encrypted_msg.getBinList())

    # save encoded image
    enc_image.save('encodedCat.png')

    # display encoded image
    enc_image.show()

# ------------------------------------------------------------------------------------------- ############### callEncodeLSB(message, image_input)

# callEncodeLSB
# calls the encode function with internally provided message and image
### message: input message string
### image_input: filepath for image to be encoded
### return: encoded image
def callEncodeLSB(message, image_input):
    
    # encrypt message
    encrypted_msg = EncryptedMessage(str(message))

    # save key
    key = encrypted_msg.getKey()
    
    # take image input
    image_file = image_input
    image = Image.open(image_file, 'r')

    # encode encrypted message in image
    enc_image = encode(image, encrypted_msg.getBinList())

    # return statement
    return enc_image, key.decode("utf-8");

# ------------------------------------------------------------------------------------------- ############### encode(image, data)

# encode
# encodes a list of binary values into an image with the LSB (least significant bit) approach
### image: image object
### data: list of binary values to encode into an image
def encode(image, data):
    
    # copies input image
    enc_image = image.copy()
    enc_image = enc_image.convert('RGB')

    # sets width and height values
    width, height = enc_image.size

    # copies pixel data for input image
    pixels = enc_image.load()
    
    # initializes variables for loop
    w_index = 0
    h_index = 0
    bit_index = 0
    
    # select 3 pixels at a time (right now only works on one line of image, so only shorter messages will works)
    # print(pixels[0, 0])
    for i in range(len(data)):
        
        # set bit_index to 0
        bit_index = 0

        # iterates through 3 pixels, changes least significant bit of RGB binary values
        for count in range(3):

            # get RGB values for current pixel
            r,g,b = pixels[w_index, h_index]
            
            # convert rgb into binary
            r_bit = bin(r)
            g_bit = bin(g)
            b_bit = bin(b)

            # change least significant bit of each byte
            if(bit_index < 8):
                r_bit = r_bit[0 : len(r_bit) - 1] + data[i][bit_index]
                bit_index += 1
            
            if(bit_index < 8):
                g_bit = g_bit[0 : len(g_bit) - 1] + data[i][bit_index]
                bit_index += 1
            
            if(bit_index < 8):
                b_bit = b_bit[0 : len(b_bit) - 1] + data[i][bit_index]
                bit_index += 1

            # save updated pixel
            pixels[w_index, h_index] = (int(r_bit, 2), int(g_bit, 2) , int(b_bit, 2))

            # update w_index
            if w_index == (width - 1):
                w_index = 0
                h_index += 1
            else:
                w_index += 1

    # add trail of zeroes to mark the end of the message
    # all zeroes is a NULL value, we don't expect it too occur
    for count in range(10):
        
        # set bit_index to 0
        bit_index = 0
        
        for count in range(3):

            # get RGB values for current pixel
            r, g, b = pixels[w_index, h_index]
            
            # convert rgb into binary
            r_bit = bin(r)
            g_bit = bin(g)
            b_bit = bin(b)

            # change least significant bit of each byte
            if(bit_index < 8):
                r_bit = r_bit[0 : len(r_bit) - 1] + "0"
                bit_index += 1
            
            if(bit_index < 8):
                g_bit = g_bit[0 : len(g_bit) - 1] + "0"
                bit_index += 1
            
            if(bit_index < 8):
                b_bit = b_bit[0 : len(b_bit) - 1] + "0"
                bit_index += 1

            # save updated pixel
            pixels[w_index, h_index] = (int(r_bit, 2), int(g_bit, 2) , int(b_bit, 2))

            # update w_index
            if w_index == (width - 1):
                w_index = 0
                h_index += 1
            else:
                w_index += 1

    # return encoded image
    return enc_image

# -------------------------------------------------------------------------------------------

# call main fxn
if __name__ == '__main__' :
    main()