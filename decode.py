from PIL import Image

def binaryToString(binary_values):
    string = ""
    for binary_value in binary_values:
        print(binary_value)
        base2int = int(binary_value, 2) # convert to base 2 int
        ascii_char = chr(base2int) # convert to ascii char
        string += ascii_char
    return string


image = Image.open("encodedCat.png", 'r')
pixels = image.load()
# Iterate over pixels of the first row
bin_strings = []

#The length of this number is how many characters it reads
for x in range(40):
    string = ""
    for j in range(3):
        r,g,b = pixels[(x * 3) + j, 0]
        # Store LSB of each color channel of each pixel
        string += bin(r)[-1]
        string += bin(g)[-1]
        if(j < 2):
            string += bin(b)[-1]

    #string = string[::-1]
    print(string)
    bin_strings.append(string)

print(binaryToString(bin_strings))
