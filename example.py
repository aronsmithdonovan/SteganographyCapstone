from PIL import Image
from numpy import asarray

#EXAMPLES
# # load the image
# image = Image.open('koala.jpg')
# image.show()
# # convert image to numpy array
# data = asarray(image)
# print(type(data))
# # summarize shape
# print(data.shape)
#
# # create Pillow image
# image2 = Image.fromarray(data)
#
# print(type(image2))
#
# # summarize image details
# print(image2.mode)
# print(image2.size)

# example of converting plain text string into binary to be hidden in image
def stringToBinary(str):
    res = ' '.join(format(ord(i), 'b') for i in str)
    return res

def binaryToString(binary_string):
    binary_values = binary_string.split() # split on whitespace into array
    string = ""
    for binary_value in binary_values:
        base2int = int(binary_value, 2) # convert to base 2 int
        ascii_char = chr(base2int) # convert to ascii char
        string += ascii_char
    return string

message = "Hello, this is a secret message"
print("Original message: " + message)
binary = stringToBinary(message)
print("Binary message: " + binary)
new_message = binaryToString(binary)
print("Reconverted message: " + new_message)
