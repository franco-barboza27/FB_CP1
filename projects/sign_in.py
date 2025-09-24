print("Greetings! Franco's totally real website that totally exists welcomes you!")


user_info = {}

print("First things first though, would like like to log in(L) or make a new account(S)?")

while True:

    while True:

        #for the loop that checkes if they want to log in or not at the end of the sign in option.
        log_choice = True
        user_choice = input("Final answer: Login or sign in?(S/L):\n")

        if user_choice == "S":
            log_choice = True

            while log_choice:

                print("Very well, we will now create a password and username!")

                while True:

                    temp_name = input("What do you want your username to be?:\n")

                    if temp_name in user_info:
                        print("I'm sorry, but that username already exists, please try a different name.")
                    else:
                        print("Ok, now please choose a password.")
                        break

                temp_pass = input("What will your password be?:\n")


                user_info[temp_name] = temp_pass

                print("Thank you, you may now use the totally existant website that exists and I totally won't just send you back to the first input!.")

                sec_check = input("Do you want to sign in or log in S/L: \n")

                s_check_loop = True

                while s_check_loop:

                    if sec_check == "S":
                        s_check_loop = False
                    elif sec_check == "L":
                        s_check_loop = False
                        log_choice = False
                    else:
                        print("Input did not match format.")
                        s_check_loop = False
                        log_choice = False

        elif user_choice == "L":
            print("Ok, logging you in.")
        else:
            print("Input did not match the format.")
            break
            


        if user_info:
        

            while log_choice:

                while True:

                    user_check = input("What is your user name? (Caps sensitive):\n")

                    if user_check in user_info:
                        print("I've checked my name database and that name DOES exist!")
                        break
                    else:
                        print("I'm sorry but that name does NOT exist. Are you sure you typed it correctly?")

                while True:

                    pass_check = input("What is your password?:\n")

                    if pass_check in user_info.values() and user_check in user_info:
                        print("Logging you in, Welcome to franco's super totally awesome website of awesomeness.")
                        log_choice = False
                        break
                    elif pass_check:
                        print("That password is incorrect GET OUT YOU HACKERRRR.\n AHEM, sorry about that, are you sure you typed your password correctly?\n")
        else:
            print("No users exist yet. Please sign in instead.")
                                

