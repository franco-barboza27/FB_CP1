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
                  "unacquired skills":{"random recollection":"costs 5 adrenaline, you do 10 questions", "save the hardest for last":"costs 2 adrenaline, you do 3 questions", "guess":"costs 2 adrenaline, answer 2 questions, gain reduced sleep."},
                  }

        winlossrw = tun_fight(player, tun)
        winlossdr = False
    elif wrldr == "2":
        player = {"state":{"alive":True},
                  "stats":{"lucidity":0, "social battery":10},
                  "statmax":{"lucidity":50, "social battery":10},
                  "miscish stats":{"charm":5, "imagination":0},
                  "inventory":{},
                  "Collected items":{},
                  "usable items":{"sleep tea":"decreases lucidity by 10", "big rock":"-20 lucidity",
                                  "frying pan":"You make yourself eggs--you recharge 5 social batter", "PSPC":"recharge 10 social batter"},
                  "skills":{},
                  "unacquired skills":{"dramatic lie":"costs 10 social battery and does 30 charm", "puppy dog eyes":"Costs 2 social batter, does 7 charm", "disassociate":"gain 3 social battery, skip a turn"}, 
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

def combat(enemy, player):
    charmcount = 0
    disassociate = 0

    while True:
        if player["stats"]["lucidity"] <= player["statmax"]["lucidity"]:
            contq = cont()
            if contq == True:
                return "LOSS"
        elif enemy[1] <= charmcount:
            player["battle"] = player["battles"].append(enemy[0])
            player["miscish stats"]["imagination"] = player["miscish stats"]["imagination"] + 1
            if player["miscish stats"]["imagination"]//3 == 1:
                playerupdate = levelup(player)
                player = playerupdate
                player["miscish stats"]["imagination"] = player["miscish stats"]["imagination"] - 3
            playerupdate = playerregen(player)
            player = playerupdate

        if disassociate <= 0:
            print("Would you like to:\n1) Charm\n2) Use Skills\n3) Use Items")
            turnch = inputchecker(3)
            if turnch == 1:
                print("You used your Charm on the enemy!")
                charmcount += player["miscish stats"]["charm"]
            elif turnch == 2:
                skilly = DW_skills(charmcount, player)
                charmcount = skilly[0]
                player = skilly[1]
                disassociate = skilly[2]
            elif turnch == 3:
                itemmy = DW_items(player)
                player = itemmy
        else:
            print("You're still disassociating!")
        
        direction = random.randint(1, 2)
        change = random.randint(0, 3)

        if direction == 1:
            damage = enemy[0] + change
        elif direction == 2:
            damage = enemy[0] - change

        print(random.choice(enemy[2]))

        print(f"Your lucidity increased by {damage}!!")

def RW_route_parents():
    parent = [10, ["flavor text list"]]

def DW_route_parents(player):
    # WAITERRRR, flavor text please :)
    charmcounter = 0
    losscounter = 0
    disassociate = 0
    parents = [10, ["flavor text list"]]
    player = playerregen(player)

    while True:
        if losscounter >= 100:
            contq = cont()
            DW_route_parents(player)
        elif charmcounter >= 100:
            completion()
        
        if disassociate == 0:
            print("Would you like to:\n1) Charm\n2) Use Skills")
            turnch = inputchecker(2)

            if turnch == 1:
                print("You used your Charm on your parents!")
                charmcount += player["miscish stats"]["charm"]
            elif turnch == 2:
                skilly = DW_skills(charmcount, player)
                charmcount = skilly[0]
                player = skilly[1]
                disassociate = skilly[2]
        else:
            print("You are still disassociating!")
        
        direction = random.randint(1, 2)
        change = random.randint(0, 3)

        if direction == 1:
            damage = parents[0] + change
        elif direction == 2:
            damage = parents[0] - change

        print(random.choice(parents[1]))

        print(f"The loss counter increased by {damage}!!")

def levelup(player):
    print("You gained enough imagination to level up!")
    print("You will now get a random SKILL and a STAT BONUS of your choice")

    newskill = random.choice(list(player["unacquired skills"].keys()))
    player["skills"][newskill] = player["unacquired skills"][newskill]
    del player["unacquired skills"][newskill]

    print(f"You got the {newskill} skill!")
    print(f"{newskill}: {player["skills"][newskill]}")

    print("You may now choose a stat to upgrade by 5, 20 in the case of lucidity!")
    while True:
        statinc = input("Would you like to upgrade your:\n1) Charm\n2) Social Battery\n3) Lucidity Cap")
        try:
            statinc = int(statinc)
            if statinc in range(1, 4):
                break
            else:
                print("That's not an option :(")
                continue
        except ValueError:
            continue
        
    if statinc == 1:
        player["miscstats"]["charm"] = player["miscstats"]["charm"] + 5
        print(f"Your Charm increased by 5!")
    elif  statinc == 2:
        player["statmax"]["social battery"] = player["statmax"]["social battery"] + 5
    elif  statinc == 3:
        player["statmax"]["lucidity"] = player["statmax"]["lucidity"] + 5

    return player

def RW_items(queleft, player):
    # ADD FLAVOR TEXT
    count = 1
    for specitem in player["inventory"].keys():
        print(f"{count}) {specitem} : {player["inventory"][specitem]}")
        count += 1

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
    
    return queleft, player

def DW_items(player):
    # ADD FLAVOR TEXT
    count = 1
    for specitem in player["inventory"].keys():
        print(f"{count}) {specitem} : {player["inventory"][specitem]}")
        count += 1

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

    if item == "sleep tea":
        player["stats"]["lucidity"] = player["stats"]["lucidity"] - 10
        if player["stats"]["lucidity"] < 0:
            player["stats"]["lucidity"] = 0
            
    elif item == "big rock":
        player["stats"]["lucidity"] = player["stats"]["lucidity"] - 20
        if player["stats"]["lucidity"] < 0:
            player["stats"]["lucidity"] = 0

    elif item == "frying pan":
        player["stats"]["social battery"] = player["stats"]["social battery"] + 5
        if player["stats"]["social battery"] < player["statmax"]["social battery"]:
            player["stats"]["social battery"] = player["statmax"]["social battery"]
    elif item == "PSPC":
        player["stats"]["social battery"] = player["stats"]["social battery"] + 5
        if player["stats"]["social battery"] < player["statmax"]["social battery"]:
            player["stats"]["social battery"] = player["statmax"]["social battery"]
    
    return player

def RW_skills(queleft, player):
    # ADD FLAVOR TEXT!!!!!!
    count = 1
    for specskill in player["skills"].keys():
        print(f"{count}) {specskill} : {player["skills"][specskill]}")
        count += 1

    while True:
        sklcho = input(f"What skill would you like to choose? 1~{count}:\n")
        try:
            sklcho = int(sklcho)
            if sklcho in range(1, count+1):
                break
            else:
                print("That's not an option :(")
                continue
        except ValueError:
            continue

    skilllist = list(player["skills"].keys())
    skill = skilllist[sklcho]

    if skill == "random recollection" and player["stats"]["adrenaline"] >= 5:
        player["stats"]["adrenaline"] = player["stats"]["adrenaline"] - 5
        queleft = queleft - 10
    elif skill == "save the hardest for last" and player["stats"]["adrenaline"] >= 2:
        player["stats"]["adrenaline"] = player["stats"]["adrenaline"] - 2
        queleft = queleft - 3
    elif skill == "guess" and player["stats"]["adrenaline"] >= 2:
        player["stats"]["adrenaline"] = player["stats"]["adrenaline"] - 1
        queleft = queleft - 1
        player["stats"]["sleepiness"] = player["stats"]["sleepiness"] - 10
        if player["stats"]["sleepiness"] < 0:
            player["stats"]["sleepiness"] = 0
    
    return queleft, player

def DW_skills(charmco, player):
    # ADD FLAVOR TEXT!!!!!!!!!!!1111!!!11!!!1!1
    count = 1
    dissassociate = 0
    for specskill in player["skills"].keys():
        print(f"{count}) {specskill} : {player["skills"][specskill]}")
        count += 1

    while True:
        sklcho = input(f"What skill would you like to choose? 1~{count}:\n")
        try:
            sklcho = int(sklcho)
            if sklcho in range(1, count+1):
                break
            else:
                print("That's not an option :(")
                continue
        except ValueError:
            print("That's not a number according to Python-sama, Sorry!")
            continue

    skilllist = list(player["skills"].keys())
    skill = skilllist[sklcho]

    if skill == "dramatic lie" and player["stats"]["social battery"] >= 10:
        player["stats"]["social battery"] = player["stats"]["social battery"] - 10
        charmco = charmco + 30
    elif skill == "puppy dog eyes" and player["stats"]["social battery"] >= 2:
        player["stats"]["social battery"] = player["stats"]["social battery"] - 2
        charmco = charmco + 7
    elif skill == "disassociate":
        dissassociate = dissassociate + 1
        player["stats"]["social battery"] = player["stats"]["social battery"] + 3
        if player["stats"]["social battery"] < player["statmax"]["social battery"]:
            player["stats"]["social battery"] = player["statmax"]["social battery"]
    
    return charmco, player, dissassociate

def playerregen(player):
    for stat in player["stats"]:
        player["stats"][stat] = player["statmax"][stat]

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

def completion():
    # Make COOLER please :)
    print("WOW! You made it all the way to the end and got your car!")
    while True:
        restart = input("Would you like to play from the beginning all over again?(Y/N)")
        if restart == "Y":
            intro()
        elif restart == "N":
            print("Insert REALLY cool credits here:")
        else:
            print("What? Can you say that again? I don't think that was the letter Y OR N...")

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

def inputchecker(rangeofchoices):
    while True:
            choicevar = input(f"Which one would you like to choose?(1~{rangeofchoices})")
            try:
                choicevar = int(choicevar)
                if choicevar in range(1, rangeofchoices+1):
                    break
                else:
                    print("That's not an option :(")
                    continue
            except ValueError:
                    continue
            
    return choicevar

intro()