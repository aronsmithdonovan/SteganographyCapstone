from PIL import Image

# Take message input, and image input
def main(message, imageFile):
    # print("Enter the message you would like to encode")
    # message = str(input())

    data = stringToBinary(message).split()
    data = appendZeros(data)

    #print("Enter the name of the image file (include extension)")
    #imageFile = input()
    # imageFile = "cat.png"
    image = Image.open(imageFile, 'r')

    conceal(image, data)

def conceal(image, data):
    encImage = image.copy()
    width, height = encImage.size
    pixels = encImage.load()

    # select 3 pixels at a time (right now only works on one line of image,
    # so only shorter messages will works)
    print(pixels[0, 0])
    for i in range(len(data)):
        index = i * 3

        bit_index = 0
        bit_length = len(data[i])
        # iterates through 3 pixels, changes least significant bit of rgb
        print(data[i])
        for j in range(3):
            r, g, b = pixels[index + j, 0]

            # convert rgb into binary
            r_bit = bin(r)
            g_bit = bin(g)
            b_bit = bin(b)

            # change least significant bit of each byte
            print(data[i][bit_index])
            if(bit_index < 8):
                r_bit = r_bit[0: len(r_bit) - 1] + data[i][bit_index]
                bit_index += 1
            print(data[i][bit_index])

            if(bit_index < 8):
                g_bit = g_bit[0: len(g_bit) - 1] + data[i][bit_index]
                bit_index += 1

            if(bit_index < 8):
                print(data[i][bit_index])
                b_bit = b_bit[0: len(b_bit) - 1] + data[i][bit_index]
                bit_index += 1

            # save updated pixel
            pixels[index + j, 0] = (int(r_bit, 2), int(g_bit, 2) , int(b_bit, 2))

    encImage.save('encodedPic.png')

# converts string to binary string
def stringToBinary(str):
    res = ' '.join(format(ord(i), 'b') for i in str)
    return res

# Makes it so each char is 8 bits
def appendZeros(binary_data):
    new_data = []
    for str in binary_data:
        while(len(str) < 8 ):
            str = "0" + str
        new_data.append(str)
    return new_data

if __name__ == '__main__' :
    # Calling main function
    main()
