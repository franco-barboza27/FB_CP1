# FB 1st Hello World Advanced ;-;

# Write a program that asks the user for their name in an input, then says hello to them by name in an output! CHECK


# Create a project that says hello to an admin user if you or Ms. LaRose type in their name. Check
# Says hello to 5 different returning user. CHECK
# Says welcome for the first time for any other users.CHECK

import sys

def remembernessThing():
    print("Hi, this is a simple program that tests out lists, inputs and outputs")


    startingQuestion = input("Do you wish to begin? Y/N: \n")
    startCondition = False
    endCondition = False
    pastUsersList = []


    while startCondition == False:
        if startingQuestion == "Y":
            print("very well, we will now begin")
            userName = input("What is your name? \n")
            startCondition = True
        elif startingQuestion == "N":
            print("GO AWAY THEN!")
            startCondition = True
            endCondition = True
        else:
            print("I am sorry, but the input did not match the required format. ")
            startingQuestion = input("Do you wish to begin? Y/N: \n")

    while endCondition == False:
        if userName in pastUsersList:
            print(f"Welcome back {userName}")
        elif userName == "Mrs.LaRose":
            print(f"Oh, Hi {userName} how do you like my program so far? I feel too lazy to actually make an input for that so I'll just know using clairvoyance.")
        else:
            print("Wowza, It's your first time here!")
            pastUsersList.append(userName)

        keepGoing = input("Do you want to enter another User's name? Y/N: \n")

        if keepGoing == "Y":
            print("very well, we will continue.")
            userName = input("What is your name? \n")
        elif keepGoing == "N":
            print("Ok, the program will soon terminate.")
            endCondition = True
            startCondition = True
        else:
            print("I am sorry, but the input did not match the required format. ")
            keepGoing = input("Do you want to enter another User's name? Y/N: \n")

remembernessThing()