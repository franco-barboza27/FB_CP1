# FB 1st restaurant menu
# drink, main course and 2 sides and total cost

# function to convert choices to items on the menu
def menu_converter(choice, menudict):
    itemnum = 1
    choice = int(choice)
    for i in menudict.keys():
        if  itemnum == choice:
            return i
        itemnum += 1

# make menus CHECK
      
# so probably have 3 drinks, 3 main courses and 4 sides CHECK
menu = [
    {"Honey suckle juice":2.25, "Leaf water":1.00, "SodAphid":5.50},
    {"Hot Fly Grub":10.00, "Port Puddle Specialty Sliders":86.87, "Mosquito brine Soup":12.00},
    {"Acorn Leaf Salad":1.00, "Dirt Bowl":1.00, "Larva Slices":2.00, "Port Puddle Specialty Grilly":50.49}
]

# make introduction
print("The waiter comes over.\n'Welcome to Port Puddle's one and only Bug n' Grub!'\n 'Please have a seat.' The waiter says.")
print("You seat your carapace onto the bar stool, your mandibles twitching with hunger.")

print("Would you like:")

# presents each drink option
i=1
for item in menu[0]:
    print(f"{i}) {item} for {menu[0][item]} Rocks")
    i+=1
print(f"{i}) None")

#checks if it's a valid choice
while True:
    drinkc = input("Which would you like?1-4:\n")
    if drinkc.isnumeric():
        if int(drinkc) <= 0 or int(drinkc) >=5:
            print("'Sorry I didn't quite catch that. What did you say?'")
        else:
            break
    else:
        print("'Uhhh... That's not a number on the list.'")

print("'Thank you, that will come right up!'")

drink = menu_converter(drinkc, menu[0])

print(f"A few moments later the waiter brings you your {drink}.")

print("Now then, what will your main course be?")
# presents each main course option
i=1
for item in menu[0]:
    print(f"{i}) {item} for {menu[0][item]} Rocks")
    i+=1
print(f"{i}) None")

#checks if it's a valid choice
while True:
    coursec = input("Which would you like?1-4:\n")
    if coursec.isnumeric():
        if int(coursec) <= 0 or int(coursec) >=5:
            print("'Sorry I didn't quite catch that. What did you say?'")
        else:
            break
    else:
        print("'Uhhh... That's not a number on the list.'")