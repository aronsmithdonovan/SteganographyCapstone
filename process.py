# process.py
#
# contains methods for encrypting and decrypting text with a private key
#
# -------------------------------------------------------------------------------------------

# imports
from cryptography.fernet import Fernet
import sys

# ------------------------------------------------------------------------------------------- ############### main()

# main
# allows use of this file's encryption and decryption methods from the command line
def main():

    # running loop
    while True:
        # prompt to either encrypt or decrypt
        print("\nWould you like to encrypt a message or decrypt a message?" +
                "\nPlease type E for encrypt and D for decrypt, or type QUIT to quit.")
        encrypt_or_decrypt = str(input())
        
        # if encrypt...
        if encrypt_or_decrypt == "E":
            # gets message from user
            print("\nEnter message to encrypt:")
            message = str(input())
            
            # encrypts message
            encrypted_message = EncryptedMessage(message)

            # prints key
            key = encrypted_message.getKey()
            print("\nGenerating key...\n\nYour generated key is:\n" + 
                    key.decode('utf-8') + 
                    "\n\nSave this key to be able to decrypt your message.")
            
            # prints encrypted message
            print("\nYour encrypted message is:\n" + encrypted_message.getString())
        
        # if decrypt...
        elif encrypt_or_decrypt == "D":
            # gets message from user
            print("\nEnter message to decrypt:")
            message = str(input())
            
            # gets key from user
            print("\nPlease provide the key used to encrypt the message:")
            key = str(input())
            
            # decrypts message
            decrypted_message = DecryptedMessage(message, key)

            # prints decrypted message
            print("\nYour decrypted message is:\n" + decrypted_message.getString())

        # if quit...
        elif encrypt_or_decrypt == "QUIT":
            print("\nOkay, terminating program...")
            sys.exit()

        # else continue running loop
        else:
            continue
        
# ------------------------------------------------------------------------------------------- ############### EncryptedMessage

# EncryptedMessage
# encrypts a provided message and stores it as a string, bytes, and a list of binary values
### message: message to be encrypted; may be a string, bytes, or a list of binary values
### self.key: generated encryption key
### self.bytes_encrypted_msg: encrypted message as bytes
### self.string_encrypted_msg: encrypted message as string
### self.binlist_encrypted_msg: encrypted message as list of binary values
class EncryptedMessage:
    
    # initialization
    def __init__(self, message):
        
        # generate key
        self.key = Fernet.generate_key()

        # encrypt message and store encrypted versions
        # DO NOT STORE ORIGINAL MESSAGE IN THIS CLASS
        if str(type(message)) == str(type("")):
            self.bytes_encrypted_msg = encryptMessage(message, self.key)
            self.string_encrypted_msg = self.bytes_encrypted_msg.decode('utf-8')
            self.binlist_encrypted_msg = stringToBinaryList(self.string_encrypted_msg)
        elif str(type(message)) == str(type(b"")):
            self.bytes_encrypted_msg = encryptMessage(message.decode('utf-8'), self.key)
            self.string_encrypted_msg = self.bytes_encrypted_msg.decode('utf-8')
            self.binlist_encrypted_msg = stringToBinaryList(self.string_encrypted_msg)
        elif str(type(message)) == str(type([])):
            self.bytes_encrypted_msg = encryptMessage(binaryListToString(message), self.key)
            self.string_encrypted_msg = self.bytes_encrypted_msg.decode('utf-8')
            self.binlist_encrypted_msg = stringToBinaryList(self.string_encrypted_msg)
        else:
            self.bytes_encrypted_msg = ""
            self.string_encrypted_msg = ""
            self.binlist_encrypted_msg = []

    # get key
    def getKey(self):
        return self.key
    
    # get encrypted message as bytes
    def getBytes(self):
        return self.bytes_encrypted_msg

    # get encrypted message as string
    def getString(self):
        return self.string_encrypted_msg

    # get encrypted message as list of binary values
    def getBinList(self):
        return self.binlist_encrypted_msg

# ------------------------------------------------------------------------------------------- ############### DecryptedMessage
    
# DecryptedMessage
# decrypts a provided message and stores it as
### message: message to be decrypted; may be a string, bytes, or a list of binary values
### key: key to decrypt message
### self.key: generated encryption key
### self.bytes_encrypted_msg: encrypted message as bytes
### self.string_encrypted_msg: encrypted message as string
### self.binlist_encrypted_msg: encrypted message as list of binary values
class DecryptedMessage:
    
    # initialization
    def __init__(self, message, key):
        
        # store key
        if str(type(key) == str(type(""))):
            self.key = bytes(key, 'utf-8')
        elif str(type(key)) == str(type(b"")):
            self.key = key

        # decrypt message and store decrypted versions
        if str(type(message)) == str(type("")):
            self.bytes_decrypted_msg = decryptMessage(message, self.key)
            self.string_decrypted_msg = self.bytes_decrypted_msg.decode('utf-8')
            self.binlist_decrypted_msg = stringToBinaryList(self.string_decrypted_msg)
        elif str(type(message)) == str(type(b"")):
            self.bytes_decrypted_msg = decryptMessage(message.decode('utf-8'), self.key)
            self.string_decrypted_msg = self.bytes_decrypted_msg.decode('utf-8')
            self.binlist_encrypted_msg = stringToBinaryList(self.string_decrypted_msg)
        elif str(type(message)) == str(type([])):
            self.bytes_decrypted_msg = decryptMessage(binaryListToString(message), self.key)
            self.string_decrypted_msg = self.bytes_decrypted_msg.decode('utf-8')
            self.binlist_decrypted_msg = stringToBinaryList(self.string_decrypted_msg)
        else:
            self.bytes_decrypted_msg = ""
            self.string_decrypted_msg = ""
            self.binlist_decrypted_msg = []

    # get key
    def getKey(self):
        return self.key
    
    # get decrypted message as bytes
    def getBytes(self):
        return self.bytes_decrypted_msg

    # get decrypted message as string
    def getString(self):
        return self.string_decrypted_msg

    # get decrypted message as list of binary values
    def getBinList(self):
        return self.binlist_decrypted_msg

# ------------------------------------------------------------------------------------------- ############### encryptMessage(message, key)

# encryptMessage
### message: string to be encrypted
### key: encryption key, must be generated by Fernet
### return: encrypted message as bytes
def encryptMessage(message, key):
    
    # sanitize message
    sani_message = cleanMessage(str(message))
    b_sani_message = bytes(sani_message, 'utf-8')

    # process key
    k = Fernet(key)

    # encrypt message
    encrypted_msg = k.encrypt(b_sani_message)

    # return encrypted message
    return encrypted_msg

# ------------------------------------------------------------------------------------------- ############### decryptMessage(message, key)

# decryptMessage
### message: string to be decrypted
### key: key used to encrypt the provided message
### return: the decrypted message as bytes
def decryptMessage(message, key):
    
    # sanitize message
    sani_message = cleanMessage(str(message))
    b_sani_message = bytes(sani_message, 'utf-8')

    # process key
    k = Fernet(key)

    # decrypt message
    decrypted_msg = k.decrypt(b_sani_message)

    # return decrypted message
    return decrypted_msg

# ------------------------------------------------------------------------------------------- ############### cleanMessage(message)

# cleanMessage
# sanitizes a string OR terminates program if unacceptable characters are found in string
### message: string to be sanitized
### return: the sanitized string
def cleanMessage(message):
    
    # cast argument to string (precaution)
    message = str(message)

    # convert string to list of characters
    message_list = list(message)

    # convert list of characters to list of decimal ASCII values
    ascii_list = []
    for each in message_list:
        ascii_list.append(ord(each))
    
    # check ASCII values, then modify if needed and pop onto sani_list
    ### program will terminate if unacceptable ASCII values are in the string
    index = 0
    sani_list = []
    for index in range(0, len(ascii_list)):
        # check for unacceptable characters
        if ascii_list[index] >= 176 or 31 >= ascii_list[index] >= 16 or ascii_list[index] == 12 or 8 >= ascii_list[index] >= 0:
            print("\nunacceptable character found in input.\nterminating program...")
            sys.exit()
        # adds \ before characters that need to be escaped (double quote, single quote, backslash, respectively)
        elif ascii_list[index] == 34 or ascii_list[index] == 39 or ascii_list[index] == 92:
            sani_list.append("\\" + message_list[index])
            index += 1
        else:
            sani_list.append(message_list[index])
            index +=1

    # convert sanitized list of characters to sanitized message
    sani_message = ""
    for each in sani_list:
        sani_message += each

    # return sanitized message
    return sani_message

# ------------------------------------------------------------------------------------------- ############### appendZeroes(binary_list)


# makes each item in a list of binary values 8 bits long
def appendZeroes(binary_list):
    binary_char_list = []
    for str in binary_list:
        while(len(str) < 8 ):
            str = "0" + str
        binary_char_list.append(str)
    return binary_char_list

# ------------------------------------------------------------------------------------------- ############### stringToBinaryList(string)

# converts string to a list of binary
def stringToBinaryList(string):
    binary_string = ' '.join(format(ord(i), 'b') for i in string)
    binary_list = binary_string.split()
    binary_char_list = appendZeroes(binary_list)
    return binary_char_list

# ------------------------------------------------------------------------------------------- ############### binaryListToString(binary_list)

# converts a list of binary values to an ASCII string
def binaryListToString(binary_list):
    string = ""
    for each in binary_list:
        base2int = int(each, 2) # convert to base 2 int
        ascii_char = chr(base2int) # convert to ascii char
        string += ascii_char
    return string

# -------------------------------------------------------------------------------------------

# call main fxn
if __name__ == '__main__':
    main()    

# -------------------------------------------------------------------------------------------

# end of file