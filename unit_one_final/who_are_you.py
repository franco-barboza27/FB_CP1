# FB 1st Unit One Project Advanced (hopefully)

# get the user's name
# get the user's age
# get their favorite color

# save info and if the username repeats, don't ask the questions again but instead just print the finished sentence output it in one complete sentence
# make a dictionary with every name input as a key and the key having color and age as the info

print("\n \nHello user, this is a database kind of project.")
print("Your information will be saved until you terminate the program.")
print("Enter 0 as Name if you want to exit")
print("We will now begin.")



def whoAreThey():

    old_users_list = []

    while True:

        check = False

        name = input("\n\nWhat is your name?\n")

        if name == "0":
            break

        for user in old_users_list:
            if name == user["name"]:
                print("\nOh! that's a re-occuring user!")
                check = True
                user_dict = user

        if check == False:
            age = input("\nHow old are you?\n")
            fav_color = input("\nWhat is your favorite color?\n")
            user_dict = {
                "name": name, 
                "age": age, 
                "fav_color": fav_color
                }
            old_users_list.append(user_dict)
        
        final_sentence = print(f"\n{name} is {user_dict["age"]} and their favorite color is {user_dict["fav_color"]}")
whoAreThey()