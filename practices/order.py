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
      
# so probably have 4 drinks, 4 main courses and 4 sides CHECK
menu = [
    {"Honey suckle juice":2.25, "Leaf water":1.00, "SodAphid":5.50, "Choccy Milkweed Milk":2.50},
    {"Hot Fly Grub":10.00, "Port Puddle Specialty Sliders":86.87, "Mosquito brine Soup":12.00, "Tree Bark Ribs":20.00},
    {"Acorn Leaf Salad":1.00, "Dirt Bowl":1.00, "Larva Slices":2.00, "Port Puddle Specialty Grilly":50.49, "Fried Shells":3.00}
]

order = []

# make introduction
print("The waiter comes over.\n'Welcome to Port Puddle's one and only Bug n' Grub!'\n 'Please have a seat.' The waiter says.")
print("You seat your carapace onto the bar stool, your mandibles twitching with hunger.")

print("Would you like:")

# presents each drink option
i=1
for item in menu[0]:
    print(f"{i}) {item} for {menu[0][item]:.2f} Rocks")
    i+=1
print(f"{i}) None")

# checks if it's a valid choice for the drink
while True:
    drinkc = input("Which would you like?1-5:\n")
    if drinkc.isnumeric():
        if int(drinkc) <= 0 or int(drinkc) >=6:
            print("'Sorry I didn't quite catch that. What did you say?'(maybe try a number in the list I JUST gave you.)")
        else:
            break
    else:
        print("'Uhhh... That's not a number... could you repeat that?'")

# make sure theres a safe guard for when the choose "None"

drink = menu_converter(drinkc, menu[0])
if drink is not "None":
    print("'Thank you, that will come right up!'")
    order.append(drink)
    print(f"A few moments later the waiter brings you your {drink}.")


print("Now then, what will your main course be?")
# presents each main course option
i=1
for item in menu[1]:
    print(f"{i}) {item} for {menu[1][item]:.2f} Rocks")
    i+=1
print(f"{i}) None")

# checks if it's a valid choice for the course
while True:
    coursec = input("Which would you like?1-5:\n")
    if coursec.isnumeric():
        if int(coursec) <= 0 or int(coursec) >=6:
            print("'Sorry I didn't quite catch that. What did you say?'\n(maybe try a number in the list I JUST gave you.)")
        else:
            break
    else:
        print("'Uhhh... That's not a number... could you repeat that?'")

print("'Thank you, that will come right up!'")
mcourse = menu_converter(coursec, menu[1])
order.append(mcourse)
    
# present the sides and do it twice
sidenum = 1
print("You may choose two sides along with that.")
while sidenum in range(1,3):
    i=1
    for item in menu[2]:
        print(f"{i}) {item} for {menu[2][item]:.2f} Rocks")
        i+=1

    # checks if it's a valid choice for the course
    while True:
        sidec = input("Which would you like?1-5:\n")
        if sidec.isnumeric():
            if int(sidec) <= 0 or int(sidec) >=6:
                print("'Sorry I didn't quite catch that. What did you say?'\n(maybe try a number in the list I JUST gave you.)")
            else:
                break
        else:
            print("'Uhhh... That's not a number... could you repeat that?'")
    side = menu_converter(sidec, menu[2])
    order.append(side)
    sidenum += 1

print("Moments later your food arrives, looking as good as you imagined")

# when checking the price,
indextracker = -1
total = 0
for fooditem in order:
    if indextracker != 2:
        indextracker += 1
    if fooditem in menu[indextracker]:
        print(f"{fooditem}: {menu[indextracker][fooditem]:.2f} R")
        total += menu[indextracker][fooditem]
    
    # otherwise be fine and give them their total
        # also dont even print anything if they order "None"
# if price is zero be like "get out of my restaraunt!"
if total == 0:
    print(f"Your total is {total} R. You're wasting my time!\n Get out of my resuaraunt!!!!")
elif total > 0:
    print(f"Your total will be {total} R.")
