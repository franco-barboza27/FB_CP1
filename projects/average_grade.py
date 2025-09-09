# FB 1st average grade advanced

# Make intro that explains how the project works and if they wish to start
# Ask how many classes they have and convert that into the specified amount of loops
# Make a way for each period to be specifically named 1, 2, 3, 4, 5, 6, 7, 8...
# Ask their grade in their classes in order of first to last period (not repeating)
# calculate their average grade
# print it out into a sentence telling them their average grade
import time as t
import sys as s


print("Hello, welcome to the average grade percentage calculator.")
print("This program will calculate you average grade percent across all of your classes.")
print("type STOP at most points to end the program.")
start = input("Do you wish to use the calculator? Y/N:\n")

while True:

    if start == "admin":
        break
    elif start == "Y":
        print("We will now begin, loading questions.")
        print("...\n\n")
        t.sleep(1)
        break
    elif start == "N" or start == "STOP":
        print("Ok, buh bye!")
        exit
        break
    else:
        print("Im sorry but your input did not match the required format")

def calcSystem():

    end = False
    
    while True:

        if end == True:
            break
        
        class_amount = []

        grades = []

        period = 0

        if start == "N":
            break

        class_num = int(input("How many classes do you have?"))
        while period < class_num:

            class_amount.append(period)
            period += 1
            question = float(input(f"What is your % grade in your period {period} class?"))
            grades.append(question)
        
        grade_total = float(sum(grades))

        print("Your percent grade average is ", round(grade_total/period, 3))

        while True:

            repeat = input("Do you wish to calculate again? Y/N:\n")

            if repeat == "Y":
                print("We will now restart, reloading questions.")
                print("...\n\n")
                t.sleep(1)
                break
            elif repeat == "N" or repeat == "STOP":
                print("Ok, buh bye!")
                end = True
                break
            else:
                print("Im sorry but your input did not match the required format")


calcSystem()