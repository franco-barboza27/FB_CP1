# FB 1st Cesar Cipher with a brute force feature

import sys

# Cipher function

def shift(shiftval, sentence):
    #all needed variables
    ascii_list = []
    indieshift = 0
    shiftval = int(shiftval)
    newstr = ""

    if shiftval < 0:
        indieshift = -1
    elif shiftval > 0:
        indieshift = 1
    else:
        return(sentence)


    for char in sentence:
        ascii_list.append(ord(char))
# Done at the same time
    # Convert the sentence into a list of each character
    # Convert all alphabet characters into their ASCII version

    # go through each item in the new list
    for num in ascii_list:
        # have a place where the original character is stored
        letter = chr(num)
        i = 0

        # use original character to check what kind it is
        while True: 
            if letter.islower():
                    
            # change the value of the ascii number as many times as specified with a loop
                while range(i, shiftval, indieshift):
                    num += indieshift
                    i += indieshift
                
                # make sure it stays in the correct letter range
                    if num < 97:
                        num = 122
                    elif num > 122:
                        num = 97
            # add the current letter/character to the string that the user will get by converting ascii back to characters
                newletter = chr(num)
                newstr = f"{newstr}"+f"{newletter}"
                break
            elif letter.isupper():
                # change the value of the ascii number as many times as specified with a loop
                    while range(i, shiftval, indieshift):
                        num += indieshift
                        i += indieshift

                    # make sure it stays in the correct letter range
                        if num < 65:
                            num = 90
                        elif num > 90:
                            num = 65
                # add the current letter/character to the string that the user will get by converting ascii back to characters
                    newletter = chr(num)
                    newstr = f"{newstr}" + f"{newletter}"
                    break
            else:
            # add the current letter/character to the sentence that the user will get by converting ascii back to characters
                symb = chr(num)
                newstr = f"{newstr}" + f"{symb}"
                break
# return the new and finished sentence
    return(newstr)
                

                
            
        
# bruteforce solve the ceaser cipher by just looping through the decode function with each possible shift
def brute_decode(sentence):
    current_shift_num = 0
    while current_shift_num in range(26):
        current_shift_num += 1
        print(shift(current_shift_num, sentence))

# Ask if they would like to use the program
start = input("This is a Ceasar cipher encoder and decoder.\nWould you like to start the program? Y/N:\n")

while True:

    while True:
        if start == "Y":
            # Ask if they would like to encode or decode 
            choice = input("Would you like to encode or decode?E/D:\n")
            if choice == "D" or "E":
                break
            else:
                print("Invalid action")
        elif start == "N":
            print("Ok bye.")
            sys.exit()
        else:
            print("THAT IS AN INVALID INPUT!! WHY WOULD YOU DO THIS TO ME????!?!??!?!>!?!")
            start = input("Would you like to start the program? Y/N:\n")

    while True:

        if choice == "D":
            # Ask for their sentence and how many shifts there are
            encoded_sen = input("What do you need to decode?E/D:\n")
            # explain that if the shift is positive, to type a negative, if its negative, type a positive
            val = int(input("What is the value of your shift?\nInput as an opposite value (EX: if the shift is 3, input -3)\nIf you do not know, enter 0:\n"))
            if val:
                # use my function from earlier
                print(f"Here is the decoded message:\n{shift(val, encoded_sen)}")
            elif val == 0:
                print(f"Here are all the possible decoded versions:\n{brute_decode(encoded_sen)}")
            else:
                print("GO away.")
        elif choice == "E":
            # Ask for their sentence and how many shifts there are
            sooncoded_sen = input("What sentence do you want to encode?\n")
            val = input("What is the value of the shift you want?\n")
            print(f"Here is the cipher:\n{shift(val, sooncoded_sen)}")
        else:
            print("Invalid action")
        
        choice = input("Would you like to encode or decode?E/D:\n")