# FB 1st Password Strength Checker

import re

past_pass = []

# Make the main forever loop

while True:
    print("Hello, this is a password strength checker!")

    # Ask a user for a password

    password = input("What is your password?:\n")
    past_pass.append(password)
    score = 0




    if len(password) >= 8:

        # check how many items
            # if less than 8, say to add more characters to their password and remove a point from their out of 5 score {will do at the end of all the loops by checking each stat and displaying the correct response}

        score += 1
        print("You have a long enough password.")
    else:
        print("Your password is NOT long enough to get a point in this category.")


    if re.findall("[A-Z]", password):
        
        # check every item and see if it's an uppercase letter
            # if there is none, say they should have an uppercase letter add a point to their score

        score += 1

        print("You have a capital letter in your password.")
    else:
        print("Your password does not have an uppercase letter, you get no points in this category.")


    if re.findall("[a-z]", password):

        # check every item and see if it's a lower case letter
            # if there is none, say they should have a lowercase letter and remove a point from their 5 score

        print("Your password has a lower case letter.")
        score += 1
    else:
        print("Your password does not have a lower case letter, you get no points in this category.")
    
    if re.findall("[0-9]", password):

        # check if it has numbers
            # if there is none, say they should have a number and remove a point from their 5 score

        print("Your password has a number.")
        score += 1
    else:
        print("Your password does not have number, you get no points in this category.")

    if re.findall("[-!@#$%^&*(){}_+=|\:;?/>.<,`~]", password) or "[" in password or "]" in password:

        # check if it has special characters
            # if there is none, say they should have a special character and remove a point from their 5 score

        print("Your password has a special character!")
        score += 1
    else:
        print("Your password does NOT have a special character, you get no points in this category.")



    print(f"You have a password strength score of {score}.")


    # tell them what the numbers mean
    if score == 0:
        print("Your password is exetremely weak, wait.... it doesn't even exist basically")
    elif score == 1:
        print("Your password is very weak.")
    elif score == 2:
        print("Your password is weak.")
    elif score == 3:
        print("Your password is mid.")
    elif score == 4:
        print("Your password is strong.")
    elif score == 5:
        print("Your password is very strong!!! Good job :D")


    print("\n\n\nHere is your password history!")

    for i in past_pass:
        print(i)
    print("\n\n\n\n\n")