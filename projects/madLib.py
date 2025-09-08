#FB 1st Mad Lib Advanced

print("Hello this is a funny fun madlib. ")
print("Also sorry but I have a chem test tomorrow so I'm not doin allat for the whole 'do you wish to begin' thing. ")

users_words = [""]
curnt_wrd = ""

for amount_word, word in enumerate(users_words):
    if amount_word <= 0:
        curnt_wrd = input("Give me an adjective: \n")
        users_words.append(curnt_wrd)
    elif amount_word < 4:
        curnt_wrd = input("\nGive me a name: \n")
        users_words.append(curnt_wrd)
    elif amount_word < 7:
        curnt_wrd = input("\nGive me an object: \n")
        users_words.append(curnt_wrd)
    elif amount_word < 8:
        curnt_wrd = input("\nGive me an action with -ing: \n")
        users_words.append(curnt_wrd)
    elif amount_word < 9:
        curnt_wrd = input("\nGive me a relative or person (maid, uncle, butler, waiter, boss, etc:). \n")
        users_words.append(curnt_wrd)
    elif amount_word < 10:
        curnt_wrd = input("\nGive me a number: \n")
        users_words.append(curnt_wrd)

print("Once upon a time, there was a " + users_words[1] + " princess named " + users_words[2] + ". She was from " + users_words[3] + " and she lived in a beautiful kingdom on the hills called " + users_words[4] + ". She had five " + users_words[5] + "s. While she was " + users_words[8] + " on the horse she fell off, so her dress had a " + users_words[6] + " stain on it. As soon as she got back to the kingdom she quickly changed so she could wash her dress. Her " + users_words[9] + " told her to come down for dinner after, and they finished eating they all went to take " + users_words[7] + ". The following day the princess went out to the village to go to the supermarket when she ran into a prince. They fell in love and got married and had " + users_words[10] + " children and they lived happily ever after in" + users_words[3] +".")