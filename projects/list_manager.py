# FL class Shopping List Manager

shop_list = []
bought_list = []

print("Hello! This is a handy dandy shopping list manager that YOU can use to manage your shops!\nYou can type 'exit' any time to leave the program.\n\n")

while True:
    action = input("Do you want to...\nAdd a new item to the list(1)\nRemove an item(2)\nCheck an item as done(3)\nUncheck an item as done(4)\nShow list(5)\nOr clear list(6)?\nEnter here:")

    if action == "exit":
        break
    elif action == "1":
        print("\n\nVery well, what do you want to add to the list?")
        added_item = input("Enter:")
        shop_list.append(added_item)
        print(f"Your item--{added_item}--was added to your shopping list!")

    elif action == "2":
        print("\n\nWhat would you like to remove?")
        removed_item = input("Enter:")

        if removed_item in shop_list:
            shop_list.remove(removed_item)
            print(f"Your item--{removed_item}--has been removed!")
        else:
            print("The item doesn't seem to exist in your list. Are you sure you typed it correctly?")

    elif action == "3":
        print("Very well, what item do you want to check off?")
        checked_item = input("Enter:")
        
        if checked_item in shop_list:
            shop_list.remove(checked_item)
            bought_list.append(checked_item)
        else:
            print("The item doesn't seem to exist in your list. Are you sure you typed it correctly?")
    elif action == "4":
            print("Ok, what item do you want to re-add to your list?")
            b_item = input("Enter:")

            if b_item in bought_list:
                bought_list.remove(b_item)
                bought_list.append(b_item)
            else:
                print("The item doesn't seem to exist in your checked item list. Are you sure you typed it correctly?")
    elif action == "5":
        for i in enumerate(shop_list)
            print()
    else:
        print("That did NOT match the format :^(")