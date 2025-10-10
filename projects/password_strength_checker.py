# FB 1st Password Strength Checker

# Make the main forever loop

# Ask a user for a password

# turn the password into a list

# check every item in the list for a specific thing using methods probably

    # check how many items and store that
        # if less than 8, say to add more characters to their password and remove a point from their out of 5 score

    # check every item and see if it's an uppercase letter
        # if there is none, say they should have an uppercase letter and remove a point from their 5 score

    # check every item and see if it's a lower case letter
        # if there is none, say they should have a lowercase letter and remove a point from their 5 score

    # check if it has numbers
        # if there is none, say they should have a number and remove a point from their 5 score

    # check if it has special characters
        # if there is none, say they should have a special character and remove a point from their 5 score

# save their password to a database and then display their ending score with what their password is missing and what the score they get means (weak, medium, strong, etc)

# display a visual representation of their password strength




import time as t

past_pass = []

while True:
    print("Hello, this is a password strength checker!")
    password = input("What is your password?:\n")

    cur_pass = []
    index = 0
    while index < len(password):
        str(password.split(index, index+1))

        index += 1
        