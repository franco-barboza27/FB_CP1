# FB 1st Cesar Cypher 

# Cipher function

    # Ask user if they want to encode or decode

        # if encode FUNCTION
            # Ask for their sentence and how many shifts there are
            # Then, convert the sentence into a list of each character
            # Convert all alphabet characters into their ASCII version
            # MAKE THIS A FUNCTION
                # For item in list of ascii
                    # for range in 1,shiftvalue+1 add 1 to the ascii num of the current list item
                    # then if it's not in the range of 65-90 or 97-122
                        # if chr(asciinum) is lowercase
                            # set asciinum to 97
                            # continue iterating
                        # else if chr(asciinum) is uppercase
                            # set asciinum to 65
                            # continue iterating
                # Turn list into a string
                # return string

        # if decode FUNCTION
            # ask if they know how many shifts there are Y/N
            # if they don't know, do a brute force decode--- TBD how to do

            # if they do
                # ask how many in a negative format (explain that if the shift is positive, to type a negative, if its negative, type a positive)
                # use my function from earlier

def shift(shiftval):
    print("placeholder")

# function





# Make a function to start the program
def prog_start():
    start = input("Would you like to start the program? Y/N:\n")
    while True:
        if start == "Y":
            # Call the function that is like the one
            print("Placeholder")
        elif start == "N":
            print("Ok bye.")
            exit
        else:
            print("THAT IS AN INVALID INPUT!! WHY WOULD YOU DO THIS TO ME????!?!??!?!>!?!")