import time, sys, random

def startup_room():
    tun = [5, 10, ["sample 1", "sample 2", "sample 3", "sample 4", "sample 5"]]
    nan = [5, 50, ["sample 1", "sample 2", "sample 3", "sample 4", "sample 5"]]

    wrldr = False

    print("You should wake up!\nNo! You should keep sleeping, just a bit longer!")

    if wrldr == False:
        wrldr = input("Will you\n1) wake up\nor\n2) keep sleeping?(1/2)")

    if wrldr == "1":
        player = {"state":{"alive":True},
                  "stats":{"sleepiness":0, "adrenaline":10, "memory":10},
                  "statmax":{"sleepiness":50, "adrenaline":10, "memory":10},
                  "inventory":{},
                  "Collected items":{},
                  "usable items":{"coffee":"decreases sleepiness by 10", "cheat sheet":"when you use the cheat sheet you answer a random amount of questions with a random chance of getting caught-losing the battle",
                                  "energy drink":"gives you 2 adrenaline and -15 sleepiness", "candy bag":"gives you 3 memory", "burrito":"decreases sleep by 10 and increases adrenaline by 3"},
                  "skills":{},
                  "unacquired skills":{"Random recollection":"costs 5 adrenaline, you do 10 questions", "Save the hardest for last":"costs 2 adrenaline, you do 4 questions", "Guess":"costs 2 adrenaline, answer 2 questions, don't gain sleep."},
                  }

        winlossrw = tun_fight(player, tun)
        winlossdr = False
    elif wrldr == "2":
        player = {"state":{"alive":True},
                  "stats":{"lucidity":0, "social battery":10, "charm":10, "imagination":0},
                  "statmax":{"lucidity":50, "social battery":10},
                  "inventory":{},
                  "Collected items":{},
                  "usable items":{"Sleep tea":"decreases lucidity by 10", "Big rock":"-20 lucidity",
                                  "Frying pan":"You make yourself eggs--you recharge 5 social batter", "Portable sound proof chamber":"recharge 5 social batter"},
                  "skills":{},
                  "unacquired skills":{"Heart-Breaking Lie":"costs 5 social battery and does 10 charm", "Puppy dog eyes":"Costs 2 social batter, does 2 charm", "Disassociate":"gain 3 social battery, skip a turn"}, 
                  "battles":[]
                  }
        winlossdr = nan_fight(player, nan)
        winlossrw = False
    
    if winlossdr == "WIN":
        nice_forest(player)
    elif winlossrw == "WIN":
        bedroom(player)

def bedroom():
    pass

def kitchen():
    pass

def campus():
    pass

def bleachers():
    pass

def library():
    pass

def food_court():
    pass

def nice_forest():
    pass

def evil_forest():
    pass

def hut():
    pass

def cellar():
    pass

def cave():
    pass

def deeper_cave():
    pass

def RW_items(queleft, player):
    
    count = 1
    for specitem in player["inventory"].keys():
        print(f"{count}) {specitem} : {player["inventory"][specitem]}")

    while True:
        itemch = input(f"What item would you like to choose? 1~{count}:\n")
        try:
            itemch = int(itemch)
            if itemch in range(1, count+1):
                break
            else:
                print("That's not an option :(")
                continue
        except ValueError:
            continue

    inventorylist = list(player["inventory"].keys())
    item = inventorylist[itemch]

    if item == "coffee":
        player["stats"]["sleepiness"] = player["stats"]["sleepiness"] - 10
        if player["stats"]["sleepiness"] < 0:
            player["stats"]["sleepiness"] = 0
            
    elif item == "energy drink":
        player["stats"]["adrenaline"] = player["stats"]["adrenaline"] + 2
        if player["stats"]["adrenaline"] > player["statmax"]["adrenaline"]:
            player["stats"]["adrenaline"] = player["statmax"]["adrenaline"]
        player["stats"]["sleepiness"] = player["stats"]["sleepiness"] - 15
        if player["stats"]["sleepiness"] < 0:
            player["stats"]["sleepiness"] = 0

    elif item == "candy bag":
        player["stats"]["memory"] = player["stats"]["memory"] + 3
        if player["stats"]["memory"] > player["statmax"]["memory"]:
            player["stats"]["memory"] = player["statmax"]["memory"]
    
    elif item == "burrito":
        player["stats"]["adrenaline"] = player["stats"]["adrenaline"] + 4
        if player["stats"]["adrenaline"] > player["statmax"]["adrenaline"]:
            player["stats"]["adrenaline"] = player["statmax"]["adrenaline"]
        player["stats"]["sleepiness"] = player["stats"]["sleepiness"] - 7
        if player["stats"]["sleepiness"] < 0:
            player["stats"]["sleepiness"] = 0

    elif item == "cheat sheet":
        caughtq = random.randint(1, 10)
        if caughtq == 1:
            print("You got caught! Whelp, guess you lost :c")
            player["stats"]["sleepiness"] = player["statmax"]["sleepiness"]
        else:
            damage = random.randint(5, 10)
            queleft = queleft - damage


def DW_items():
    pass

def RW_skills():
    pass

def DW_skills():
    pass

def tun_fight(playerchar, tunlytun):
    # add some sleep statements around here
    turn = 0

    while True:
        if playerchar["stats"]["sleepiness"] >= playerchar["statmax"]["sleepiness"]:
            contq = cont()
            if contq == True:
                return "LOSS"
            else: 
                sys.exit()
        if turn >= tunlytun[1]:
            return 

        print("This is your chance to show what you can do!") # lowkey make a flavor text randomizer here pls
        print("You will be able to use your Memory to 'recall'-- your skills and items do a variety of things!")
        print(f"You currently have:")
        print(f"Sleepiness:{playerchar["stats"]["sleepiness"]}/{playerchar["statmax"]["sleepiness"]}\nAdrenaline:{playerchar["stats"]["adrenaline"]}/{playerchar["statmax"]["adrenaline"]}\n{playerchar["stats"]["memory"]}/{playerchar["statmax"]["memory"]}")
        while True:
            turnchoice = input("Would you like to\n1) Recall\n2) Skills\n3) Items:\n")
            if turnchoice == "1":
                print("You tried to remember something you forgot!")
                playerchar["stats"]["memory"] = playerchar["stats"]["memory"]-1
                break
            elif turnchoice == "2":
                print("You actually don't have any skills yet :P")
                break
            elif turnchoice == "3":
                print("You don't have any items, sorry XD")
                break
            else:
                print("That is NOT an option sadly")
            
        direction = random.randint(1, 2)
        change = random.randint(0, 5)

        if direction == 1:
            damage = tunlytun[0] + change
        elif direction == 2:
            damage = tunlytun[0] - change

        print(random.choice(tunlytun[2]))

        print(f"Your sleepiness increased by {damage}")

        turn += 1
        
def math_t():
    pass

def chem_t():
    pass

def history_t():
    pass

def nan_fight(playerchar, nanlynan):
    charmcount = 0

    while True:
        if playerchar["stats"]["lucidity"] > playerchar["statmax"]["lucidity"]:
            contq = cont()
            if contq == True:
                return "LOSS"
    
        if charmcount >= nanlynan[1]:
            return "WIN"

        print("You still need to convince Nan to let you sleep!") # lowkey make a flavor text randomizer here pls
        print("Use your CHARM to CHARM the enemy into letting you do what you want!")
        print(f"The charm gauge is currently at {charmcount}!")
        print(f"You currently have:")
        print(f"Lucidity:{playerchar["stats"]["lucidity"]}/{playerchar["statmax"]["lucidity"]}\nSocial Battery:{playerchar["stats"]["social battery"]}/{playerchar["statmax"]["social battery"]}")

        turnchoice = input("Do you want to:\n1) Charm\n2) Use a Social Skill\n3) Use an item:\n")

        if turnchoice == "1":
            charmcount += playerchar["stats"]["charm"]
            print(f"You did {playerchar["stats"]["charm"]} charm!")
        elif turnchoice == "2":
            print("You don't have ANY social skills yet, you better train them soon!")
        elif turnchoice == "3":
            print("You don't have any items... hmm maybe you could convince someone to give you one?")
        
        direction = random.randint(1, 2)
        change = random.randint(0, 5)

        if direction == 1:
            damage = nanlynan[0] + change
        elif direction == 2:
            damage = nanlynan[0] - change

        print(random.choice(nanlynan[2]))

        print(f"Your lucidity increased by {damage}!")
        playerchar["stats"]["lucidity"] = playerchar["stats"]["lucidity"] + damage

def combat():
    pass

def cont():
    print("You unfortunately failed...")
    while True:
        contq = input("Will you try again?Y/N")
        if contq == "Y":
            print("Very well, you decided to perservere.")
            return True
        elif contq == "N":
            print("Ok then, unfortunately, you rage quitted.")
            sys.exit()
        else:
            print("Sorry, is that an option I gave you?")

def RW_route_parents():
    pass

def DW_route_parents():
    pass

def completion():
    pass

def intro():
    print("Hello, this is a TBAG--Text Based Adventure Game. (insert better intro text here)")
    while True:
        start = input("Would you like to play?(Y/N):\n")
        
        if start == "Y":
            startup_room()
        elif start == "N":
            sys.exit()
        else:
            continue

intro()