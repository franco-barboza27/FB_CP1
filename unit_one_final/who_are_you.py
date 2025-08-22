# FB 1st Unit One Project Advanced (hopefully)

# get the user's name
# get the user's age
# get their favorite color

# save info and if the username repeats, don't ask the questions again but instead just print the finished sentence

# output it in one complete sentence

print("Hello user, this is a database kind of project.")
print("Your information will be saved until you terminate the program.")
print("We will now begin.")



def whoAreThey():

    continue_forever = True

    old_users = []

    while continue_forever == True:
        name = input("What is your name?\n")
    age = input("How old are you?\n")
    fav_color = input("What is your favorite color?\n")

    final_sentence = print(f"{name} is {age} and their favorite color is {fav_color}")