# FB 1st restaurant menu

# drink, main course and 2 sides

# make menus
      
# so probably have 3 drinks, 3 main courses and 4 sides CHECK
menu = [
    {"Honey suckle juice":2.25, "Leaf water":1.00, "SodAphid":5.50},
    {"Hot Fly Grub":10.00, "Port Puddle Specialty Sliders":86.87, "Mosquito brine Soup":12.00},
    {"Acorn Leaf Salad":1.00, "Dirt Bowl":1.00, "Larva Slices":2.00, "Port Puddle Specialty Grilly":50.49}
]

# make introduction
print("Welcome to Port Puddle's one and only Bug n' Grub!\n Please have a seat.")
print("You seat your carapace onto the bar stool, your mandibles twitching with hunger.")

print("Would you like:")
i=1
for drink in menu[0]:
    print(f"{i}) {drink} for {menu[0][drink]} Rocks")
    i+=1
print(f"{i}) None")
drink = input("Which would you like?")