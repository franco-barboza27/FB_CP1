# FB class Shopping List Manager Advanced

shop_list = []
bought_list = []

print("Hello! This is a handy dandy shopping list manager that YOU can use to manage your shops!\nYou can type 'exit' any time to leave the program.\n")

while True:
    action = input("\nDo you want to...\nAdd a new item to the list(1)\nRemove an item(2)\nCheck an item as done(3)\nUncheck an item as done(4)\nShow list(5)\nOr clear list(6)?\nEnter here:")

    if action == "exit":
        break
    elif action == "1":
        print("\nVery well, what do you want to add to the list?")
        added_item = input("Enter:")
        shop_list.append(added_item)
        print(f"Your item--{added_item}--was added to your shopping list!")

    elif action == "2":
        print("\nWhat would you like to remove?")
        removed_item = input("Enter:")

        if removed_item in shop_list:
            shop_list.remove(removed_item)
            print(f"Your item--{removed_item}--has been removed!")
        else:
            print("The item doesn't seem to exist in your list. Are you sure you typed it correctly?")

    elif action == "3":
        print("\nVery well, what item do you want to check off?")
        checked_item = input("Enter:")
        
        if checked_item in shop_list:
            shop_list.remove(checked_item)
            bought_list.append(checked_item)
        else:
            print("The item doesn't seem to exist in your list. Are you sure you typed it correctly?")
    elif action == "4":
            print("\nOk, what item do you want to re-add to your list?")
            b_item = input("Enter:")

            if b_item in bought_list:
                bought_list.remove(b_item)
                shop_list.append(b_item)
            else:
                print("The item doesn't seem to exist in your checked item list. Are you sure you typed it correctly?")
    elif action == "5":

        if shop_list:
            print("\n These are the items on your list:")

            for thing, item in enumerate(shop_list, 1):
                print(f"{thing}. {item}")
        else:
            print("\nSorry, but your list is currently EMPTY!!!")
        
        if bought_list:
            print("\nThese are the things you have done!\n")

            for done_thing, bought in enumerate(bought_list, 1):
                print(f"{done_thing}. {bought}")
        else:
            print("\nYour checklist is currently empty!")

    elif action == "6":
        
        clear_list = input("\nAre you sure you want to clear your list?\nThe not yet done list(1)\nThe done list(2)\nBoth(3)\nEnter:")

        if clear_list == "1":

            while True:
                check = input("Are you sure? This will be permanent(Y/N):\n")

                if check == "Y":
                    shop_list.clear()
                    print("Your list has been cleared!")
                    break
                elif check == "N":
                    print("Very well.")
                    break
                else:
                    print("Input did not match format.")
        elif clear_list == "2":

            while True:
                check = input("Are you sure? This will be permanent(Y/N):\n")

                if check == "Y":
                    bought_list.clear()
                    print("Your done list has been cleared!")
                    break
                elif check == "N":
                    print("Very well.")
                    break
                else:
                    print("Input did not match format.")
        elif clear_list == "3":

            while True:

                check = input("Are you sure? This will be permanent(Y/N):\n")

                if check == "Y":
                    shop_list.clear()
                    bought_list.clear()
                    print("Your lists have been cleared!")
                    break
                elif check == "N":
                    print("Very well.")
                    break
                else:
                    print("Input did not match format.")
        else:
            print("Your in not did not match the format!")

    else:
        print("That did NOT match the format :^(")