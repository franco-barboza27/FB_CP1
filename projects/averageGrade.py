# FB 1st average grade advanced

# Make intro that explains how the project works and if they wish to start
# Ask how many classes they have and convert that into the specified amount of loops
# Make a way for each period to be specifically named 1, 2, 3, 4, 5, 6, 7, 8...
# Ask their grade in their classes in order of first to last period (not repeating)
# calculate their average grade
# print it out into a sentence telling them their average grade
import time as t


print("Hello, welcome to the average grade percentage calculator.")
print("This program will calculate you average grade percent across all of your classes.")
print("type STOP at any point to end the program.")
start = input("Do you wish to use the calculator? Y/N:")

while True:
    if start == "Y":
        print("We will now begin, loading questions.")
        print("...\n\n")
        t.sleep(2)
        break
    elif start == "N" or start == "STOP":
        print("Ok, buh bye!")
        exit
        break
    else:
        print("Im sorry but your input did not match the required format")

def calcSystem():

    while True:
        class_amount = []
    
        if start == "N":
            break

        class_num = int(input("How many classes do you have?"))
        for num in class_num:
            class_amount.append(num)