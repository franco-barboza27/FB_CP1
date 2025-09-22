print("Greetings! Franco's totally real website that totally exists welcomes you!")


user_info = []

while True:

    print("First things first though, would like like to log in(L) or make a new account(S)?")
    user_choice = input("Input here L/S:\n")


    while True:
        if user_choice == "S":
            print("Very well, we will now create a password and username!")

            temp_name = input("What do you want your username to be?:\n")

            if temp_name in user_info:
                print("I'm sorry, but that username already exists, please try a different name.")
            else:
                print("Ok, now please choose a password.")
                user_info.append(temp_name)

            temp_pass = input("What is your password?:\n")

            user_info.append[]

            print("Thank you, you may now use the totally existant website that exists and I totally won't just send you back to the fist input!.")

        elif user_choice == "L":
            print("Very well, logging you in:")

            while True:

                user_check = input("What is your user name? (Caps sensitive):\n")

                if user_check in user_info:
                    print("I've checked my name and that name DOES exist!")
                else:
                    print("I'm sorry but that name does NOT exist. Are you sure you typed it correctly?")

                while True:
                    pass_check = input("What is your password?")

                    if pass_check in user_info and 

                    elif pass_check not in user_info:
                        print("That password ain't even in my database, GET OUTTTTT.\n AHEM, sorry about that, are you sure you typed your password correctly?\n")
                        

