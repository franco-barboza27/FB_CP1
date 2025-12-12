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
                  "collected items":{},
                  "usable items":{"coffee":"decreases sleepiness by 10", "cheat sheet":"when you use the cheat sheet you answer a random amount of questions with a random chance of getting caught-losing the battle",
                                  "energy drink":"gives you 2 adrenaline and -15 sleepiness", "candy bag":"gives you 3 memory", "burrito":"decreases sleep by 10 and increases adrenaline by 3"},
                  "skills":{},
                  "unacquired skills":{"random recollection":"costs 5 adrenaline, you do 15 questions", "save the hardest for last":"costs 2 adrenaline, you do 5 questions", "guess":"costs 2 adrenaline, answer 3 questions, gain reduced sleep."},
                  }

        winlossrealworld= tun_fight(player, tun)
        winlossrealworld = winlossrealworld[1]
        winlossdreamworld = False
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
        winlossdreamworld = nan_fight(player, nan)
        winlossdreamworld = winlossdreamworld[1]
        winlossrealworld = False
    
    if winlossdreamworld == True:
        nice_forest(player)
    elif winlossrealworld == True:
        bedroom(player)

def bedroom(player):
    print("You woke up, your alarm blared on your table")
    print("After getting up, you look around")
    while True:
        print("1) Check desk\n2) Find glasses\n3) Go to the kitchen")
        choice = inputchecker(3)

        if choice == 1:
            if "phone" not in player["collected items"]:
                print("You found your phone")
                player["collected items"]["phone"] = "It has precious memories on it"
            else: 
                print("You aready have your phone")
        elif choice == 2:
            if "glasses" not in player["collected items"]:
                print("You found your glasses")
                print("Your maximum memory increased by 5!")
                player["statmax"]["memory"] = player["statmax"]["memory"] + 5
                player["collected items"]["glasses"] = "It helps you see better, and makes you look smarter"
            else:
                print("You already have your glasses.")
        elif choice == 3:
            print("You went to the kitchen.")
            kitchen(player)

def kitchen(player):
    print("Your kitchen, as always is somewhat messy, especially with finals coming up.")
    print("Oh, right... FINALS! Hurriedly, you look around and check what you need to do.")
    while True:
        print("1) Make Coffee\n2) Look outside\n3) Go to college")
        choice = inputchecker(3)

        if choice == 1:
            if "coffee" not in player["collected items"]:
                print("You made yourself coffee")
                player["collected items"]["coffee"] = player["usable items"]["coffee"]
                player["inventory"]["coffee"] = player["usable items"]["coffee"]
            else: 
                print("You've already made your morning coffee")
        elif choice == 2:
            print("You look outside your window... there is stuff.")
        elif choice == 3:
            print("You went out the door and walked to school")
            campus(player)

def campus(player):
    print("You have a few moments before you have to go to class and start your remaining finals")
    while True:
        print("1) Go to the bleachers\n2) Go to the library\n3) Go to the food court")
        choice = inputchecker(3)

        if choice == 1:
            print("You go to the bleachers")
            bleachers(player)
        elif choice == 2:
            print("You go to the library")
            library(player)
        elif choice == 3:
            print("You got to the food court")
            food_court(player)

def bleachers(player):
    print("As you get there, you see a couple distinct groups of people littered around the field and bleachers.")
    while True:
        print("1) Talk to the sketchy kids behind the bleachers\n2) Look around the seats\n3) Talk to the popular kids\n4) Go to the library\n5) Go to the food court\n6) Go to class")
        choice = inputchecker(6)

        if choice == 1:
            if "energy drink" not in player["collected items"]:
                print("You go and talk to the sketchy kids.")
                print("They gave you an energy drink, they've been banned for years now.")
                player["inventory"]["energy drink"] = player["usable items"]["energy drink"]
                player["collected items"]["energy drink"] = player["usable items"]["energy drink"]
            else:
                print("You've already talked to them.")
        elif choice == 2:
            if "candy bag" not in player["collected items"]:
                print("You look around the seats and find a bag full of smarties")
                print("You got the candy bag!")
                player["inventory"]["candy bag"] = player["usable items"]["candy bag"]
                player["collected items"]["candy bag"] = player["usable items"]["candy bag"]
            else:
                print("Unfortunately there wasn't anything else...")
        elif choice == 3:
            if "phone" in player["collected items"]:
                if "cheat sheet" not in player["collected items"]:
                    print("You talk to one of the cheerleaders and she adds you to a group chat with other well know schoolers.")
                    print("You look at it and see that theres a cheat sheet on it.")
                    print("You got the cheat sheet! Don't get caught!")
                    player["inventory"]["cheat sheet"] = player["usable items"]["cheat sheet"]
                    player["collected items"]["cheat sheet"] = player["usable items"]["cheat sheet"]
                else:
                    print("You talk to the cheerleader, but since you've already been added to the group chat, she just thinks you're hitting on her.")
            else:
                print("You talk to the cheerleader, although, you don't have your phone so you can't give her your number. ")
        elif choice == 4:
            print("You went to the library next, you had enough of trying to be popular")
            library(player)
        elif choice == 5:
            print("You went to the food court, after all that 'excercising' you felt famished")
            food_court(player)
        elif choice == 6:
            while True:
                starttestsq = input("Are you sure you want to start your finals now?(Y/N):")

                if starttestsq == "Y":
                    print("You go into your classroom")
                    math_t(player)
                elif starttestsq == "N":
                    print("You change your mind")
                    break
                else:
                    print("Stop being so indecisive!")

def library(player):
    print("It's mostly quiet with the occasional 'NO WAY!' sprinkled here and there.\n It's either a really good book or crazy gossip.")
    while True:
        print("1) Study your classes\n2) Study how to take tests\n3) Look around\n4) Go to the bleachers\n5) Go to the food court\n6) Go to class")
        choice = inputchecker(6)

        if choice == 1:
            if player["statmax"]["memory"] < 20:
                print("You spend a while reading through your notes and practicing active recall.")
                print("You hate it.")
                time.sleep(3)
                print("You got 1 whole maximum memory")
                player["statmax"]["memory"] = player["statmax"]["memory"] + 1
            else:
                print("NO! Enough studying this STUPID chem and STUPID math and STUPID history.")
        elif choice == 2:
            if player["unacquired skills"]:
                print("You find a book about test taking skills")
                print("It's much more manageable than studying the actual material")
                skill = str(random.choice(list(player["unacquired skills"].keys())))
                player["skills"][skill] = player["unacquired skills"][skill]
                del player["unacquired skills"][skill]
                print(f"You got:\n{skill}")
            else:
                print("There's not really anything else to learn")
        elif choice == 3:
            print("Super duper awesome and cool flavor text")
        elif choice == 4:
            print("You went to the bleachers next, because studying is for nerds")
            bleachers(player)
        elif choice == 5:
            print("You went to the food court, using your brain spends a lot of energy.")
            food_court(player)
        elif choice == 6:
            while True:
                starttestsq = input("Are you sure you want to start your finals now?(Y/N):")

                if starttestsq == "Y":
                    print("You go into your classroom")
                    math_t(player)
                elif starttestsq == "N":
                    print("You change your mind")
                    break
                else:
                    print("Stop being so indecisive!")

def food_court(player):
    print("Chatter fills the air as people understandably big back on delicious... fast food... actually maybe not too understandable.")
    while True:
        print("1) Go to the Chipotle\n2) Relax\n3) Spontaneosly break out into dance and song\n4) Go to the bleachers\n5) Go to the library\n6) Go to class")
        choice = inputchecker(6)

        if choice == 1:
            if "burrito" not in player["collected items"]:
                print("You enter the chipotle line.")
                print("The cute cashier asks for your order, so while you would normally order a taco, you accidentally just said burrito instead becaus you were nervous.")
                player["inventory"]["burrito"] = player["usable items"]["burrito"]
                player["collected items"]["burrito"] = player["usable items"]["burrito"]
            else:
                print("You don; have the guts to try asking for a refund and ordering a taco instead.")
        elif choice == 2:
            print("Since for some reason the food court has some massage chairs, you sit in one.")
            if player["statmax"]["sleepiness"] >= 80:
                print("You try to take a nap but you feel rested enough")
            else:
                print("You take a nap in a massage bed.")
                time.sleep(3)
                print("Your maximum lucidity increased by 15!")
                player["statmax"]["sleepiness"] = player["statmax"]["sleepiness"] + 15
        elif choice == 3:
            print("It's as embarrassing as it sounds")
        elif choice == 4:
            print("You went to the bleachers, excercise is probably good on a full stomache...")
            bleachers(player)
        elif choice == 5:
            print("You went to the library, studying is very important")
            library(player)
        elif choice == 6:
            while True:
                starttestsq = input("Are you sure you want to start your finals now?(Y/N):")

                if starttestsq == "Y":
                    print("You go into your classroom")
                    math_t(player)
                elif starttestsq == "N":
                    print("You change your mind")
                    break
                else:
                    print("Stop being so indecisive!")

def nice_forest(player):
    print("This route is WIP")

    print("You find yourself in the nicer part of the forest.")
    boar = ["boar", 6, ["Wow! so flavor", "text two", "even more flavor"]]
    while True:
        print("1) Look in the bush nearby\n2) Go deeper inside\n3) Go into the deep dark cave nearby\n4) Have a picnic\n")
        choice = inputchecker(4)

        if choice == 1:
            if "boar" not in player["battles"]:
                print("You ruffle the bush VERY rudely.")
                print("A gigantic boar--as in three times the size of the bush--somehow jumps out of the bush and attacks you!!.")
                fight = combat(boar, player)
                player = fight[1]
                if fight[0] == "WIN":
                    print("You charmed the wild boar! It gave you a Portable SoundProof Chamber... don't ask how.")
                    player["inventory"]["PSPC"] = player["usable items"]["PSPC"]
            else:
                print("You already charmed the boar there so it would be rude to disturb it again.")
        elif choice == 2:
            print("You go deeper into the forest.")
            evil_forest(player)
        elif choice == 3:
            print("For SOME reason you decided to go into the deep DARK CAVE")
            cave(player)
        elif choice == 4:
            print("You decided to just relax in a open part of the forest for a while...")
            time.sleep(2)
            print("It did absolutely nothing")

def evil_forest():
    print("You go into the obviously closer to progressing the game area.")
    tree = ["tree", 10, ["Wow! so flavor", "text two", "even more flavor"]]
    while True:
        print("1) Assault a tree\n2) Go EVEN deeper\n3) Go BACK to the NICE and GOOD part of the forest\n4) Go for a stroll... In the forest with horrors within your comprehension...\n")
        choice = inputchecker(4)
        if choice == 1:
            if "boar" not in player["battles"]:
                print("You kick some random tree, probably because you thought the option would be funny.")
                print("The tree REALLY didn't think it was funny.")
                fight = combat(tree, player)
                player = fight[1]
                if fight[0] == "WIN":
                    print("You charmed the angry tree! It gave you a wooden ring..... You'd rather not think about the implications")
                    player["inventory"]["PSPC"] = player["usable items"]["PSPC"]
            else:
                print("You already hit the tree why would you want to hit it again??")
        elif choice == 2:
            print("You find a HUT. \nSince theres definitely never been stories about why you shouldn't go into houses in creepy haunted forests, you head inside.")
            hut(player)
        elif choice == 3:
            print("Because you know what's good for you, you go back to the lighter part of the forest.")
            cave(player)
        elif choice == 4:
            print("You walk around and to your surprise, all of the HWIYC are very kind and dont murder you.")
            time.sleep(2)
            print("They're still scary though...")

def hut():
    print("You go into the hut... It has an old lady in it, she wont eat you maybe...")
    tree = ["old lady", 10, ["Wow! so flavor", "text two", "even more flavor"]]
    while True:
        print("1) Insult the lady\n2) Go into the creepydiki cellar\n3) Go BACK to the EVIL and BAD part of the forest\n4) Talk to the lady without insulting her\n")
        choice = inputchecker(4)
        if choice == 1:
            if "old lady" not in player["battles"]:
                print("You kick some random tree, probably because you thought the option would be funny.")
                print("The tree REALLY didn't think it was funny.")
                fight = combat(tree, player)
                player = fight[1]
                if fight[0] == "WIN":
                    print("You charmed the angry tree! It gave you a wooden ring..... You'd rather not think about the implications")
                    player["inventory"]["PSPC"] = player["usable items"]["PSPC"]
            else:
                print("You already hit the tree why would you want to hit it again??")
        elif choice == 2:
            print("You find a HUT. \nSince theres definitely never been stories about why you shouldn't go into houses in creepy haunted forests, you head inside.")
            hut(player)
        elif choice == 3:
            print("Because you know what's good for you, you go back to the lighter part of the forest.")
            cave(player)
        elif choice == 4:
            print("You walk around and to your surprise, all of the HWIYC are very kind and dont murder you.")
            time.sleep(2)
            print("They're still scary though...")

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
                update = playerregen(playerchar)
                playerchar = update
                return playerchar, False
            else: 
                sys.exit()
        if turn >= tunlytun[1]:
            print("You won!")
            update = playerregen(playerchar)
            playerchar = update
            return playerchar, True

        print("This is your chance to show what you can do!") # lowkey make a flavor text randomizer here pls
        print("You will be able to use your Memory to 'recall'-- your skills and items do a variety of things!")
        print(f"You currently have:")
        print(f"Sleepiness:{playerchar["stats"]["sleepiness"]}/{playerchar["statmax"]["sleepiness"]}\nAdrenaline:{playerchar["stats"]["adrenaline"]}/{playerchar["statmax"]["adrenaline"]}\nMemory:{playerchar["stats"]["memory"]}/{playerchar["statmax"]["memory"]}")
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

        playerchar["stats"]["sleepiness"] = playerchar["stats"]["sleepiness"] + damage

        turn += 1
        
def math_t(player):
    questions = 50
    panic = 0
    panicchance = [1 , 0 , 0 , 0 , 0]
    player = playerregen(player)
    print("Alright, I'll hand out your tests now!")
    while True:
        
        if panic == 0:
            print(f"You have:\n{questions} questions left\n{player["stats"]["memory"]}/{player["statmax"]["memory"]} memory\n{player["stats"]["sleepiness"]}/{player["statmax"]["sleepiness"]} sleepiness\n{player["stats"]["adrenaline"]}/{player["statmax"]["adrenaline"]} adrenaline")

            print("what will you do?\n1) answer questions\n2)use a skill\n3) use an item?:\n")
            turnch = inputchecker(3)

            if turnch == 1:
                if player["stats"]["memory"] > 0:
                    questions = questions - 3
                    player["stats"]["memory"] = player["stats"]["memory"] - 1
                else:
                    print("You can't remember it right now!")
            elif turnch == 2:
                update = RW_skills(questions, player)
                questions = update[0]
                player = update[1]
            elif turnch == 3:
                item = RW_skills(questions, player)
                questions = update[0]
                player = update[1]
            
            panicquestion = random.choice(panicchance)
            
            if panicquestion == 1:
                panic = random.randint(1, 3)
        else:
            panic = panic - 1
            print(f"You have {player["stats"]["sleepiness"]}/{player["statmax"]["sleepiness"]} sleepiness")

        print("You gained 5 sleepiness!")
        player["stats"]["sleepiness"] = player["stats"]["sleepiness"] - 5

        if player["stats"]["sleepiness"] >= player["statmax"]["sleepiness"]:
            contq = cont()
            if contq == True:
                math_t(player)
            if questions <= 0:
                print("you survived!")
                chem_t(player)

def chem_t(player):
    questions = 35
    playerupdate = playerregen(player)
    player = playerupdate
    print("Alright class! Backpacks to the front!\n Time for the chem test I guess...")
    while True:
        
        print(f"You have:\n{questions} questions left\n{player["stats"]["memory"]}/{player["statmax"]["memory"]} memory\n{player["stats"]["sleepiness"]}/{player["statmax"]["sleepiness"]} sleepiness\n{player["stats"]["adrenaline"]}/{player["statmax"]["adrenaline"]} adrenaline")

        print("what will you do?\n1) answer questions\n2)use a skill")
        turnch = inputchecker(2)

        if turnch == 1:
            if player["stats"]["memory"] > 0:
                questions = questions - 3
                player["stats"]["memory"] = player["stats"]["memory"] - 1
            else:
                print("You can't remember it right now!")
        elif turnch == 2:
            update = RW_skills(questions, player)
            questions = update[0]
            player = update[1]

        print("You gained 10 sleepiness!")
        player["stats"]["sleepiness"] = player["stats"]["sleepiness"] - 10

        if player["stats"]["sleepiness"] >= player["statmax"]["sleepiness"]:
            contq = cont()
            if contq == True:
                chem_t(player)
        if questions <= 0:
            print("you survived!")
            history_t(player)

def history_t():
    questions = 75
    playerupdate = playerregen(player)
    player = playerupdate()
    print("Open up your laptops gang!\n The code is kjrepsdjfgvvcLFJA")
    while True:

        if panic == 0:
            print(f"You have:\n{questions} questions left\n{player["stats"]["memory"]}/{player["statmax"]["memory"]} memory\n{player["stats"]["sleepiness"]}/{player["statmax"]["sleepiness"]} sleepiness\n{player["stats"]["adrenaline"]}/{player["statmax"]["adrenaline"]} adrenaline")

            print("what will you do?\n1) answer questions\n2)use a skill\n3) use an item?:\n")
            turnch = inputchecker(3)

            if turnch == 1:
                if player["stats"]["memory"] > 0:
                    questions = questions - 3
                    player["stats"]["memory"] = player["stats"]["memory"] - 1
                else:
                    print("You can't remember it right now!")
            elif turnch == 2:
                update = RW_skills(questions, player)
                questions = update[0]
                player = update[1]
            elif turnch == 3:
                item = RW_skills(questions, player)
                questions = update[0]
                player = update[1]

        else:
            panic = panic - 1
            print(f"You have {player["stats"]["sleepiness"]}/{player["statmax"]["sleepiness"]} sleepiness")

        print("You gained 15 sleepiness!")
        player["stats"]["sleepiness"] = player["stats"]["sleepiness"] - 15

        if player["stats"]["sleepiness"] >= player["statmax"]["sleepiness"]:
            contq = cont()
            if contq == True:
                math_t(player)
            if questions <= 0:
                print("you survived!")
                RW_route_parents(player)

def nan_fight(playerchar, nanlynan):
    charmcount = 0

    while True:
        if playerchar["stats"]["lucidity"] > playerchar["statmax"]["lucidity"]:
            contq = cont()
            if contq == True:
                update = playerregen(playerchar)
                playerchar = update
                return playerchar, False
    
        if charmcount >= nanlynan[1]:
            print("You won!")
            update = playerregen(playerchar)
            playerchar = update
            return playerchar, True

        print("You still need to convince Nan to let you sleep!") # lowkey make a flavor text randomizer here pls
        print("Use your CHARM to CHARM the enemy into letting you do what you want!")
        print(f"The charm gauge is currently at {charmcount}!")
        print(f"You currently have:")
        print(f"Lucidity:{playerchar["stats"]["lucidity"]}/{playerchar["statmax"]["lucidity"]}\nSocial Battery:{playerchar["stats"]["social battery"]}/{playerchar["statmax"]["social battery"]}")

        turnchoice = input("Do you want to:\n1) Charm\n2) Use a Social Skill\n3) Use an item:\n")

        if turnchoice == "1":
            charmcount += playerchar["miscish stats"]["charm"]
            print(f"You did {playerchar["miscish stats"]["charm"]} charm!")
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
                playerupdate = playerregen(player)
                player = playerupdate
                return "LOSS", player
        elif enemy[1] <= charmcount:
            player["battle"] = player["battles"].append(enemy[0])
            player["miscish stats"]["imagination"] = player["miscish stats"]["imagination"] + 1
            if player["miscish stats"]["imagination"]//3 == 1:
                playerupdate = levelup(player)
                player = playerupdate
                player["miscish stats"]["imagination"] = player["miscish stats"]["imagination"] - 3
            return "WIN", player
            
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
            damage = enemy[1] + change
        elif direction == 2:
            damage = enemy[1] - change

        print(random.choice(enemy[2]))

        print(f"Your lucidity increased by {damage}!!")

def RW_route_parents():
    parents = [10, ["flavor text list"]]
    evidencegauge = 0
    arguloss = 0

    while True:
        player = playerregen(player)

        if arguloss >= 100:
            contq = cont()
            DW_route_parents(player)
        elif evidencegauge >= 100:
            completion()

        print("Would you like to:\n1) Use Memory")
        turnch = inputchecker(1)

        if turnch == 1 and player["stats"]["memory"] > 0:
            print("You tried to remember a good reason why they should buy you a car!")
            evidencegauge += player["stats"]["memory"]
        
        direction = random.randint(1, 2)
        change = random.randint(0, 3)

        if direction == 1:
            damage = parents[0] + change
        elif direction == 2:
            damage = parents[0] - change

        print(random.choice(parents[1]))

        print(f"The loss counter increased by {damage}!!")

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
        player["miscish stats"]["charm"] = player["miscish stats"]["charm"] + 5
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
        del player["inventory"][item]
            
    elif item == "energy drink":
        player["stats"]["adrenaline"] = player["stats"]["adrenaline"] + 2
        if player["stats"]["adrenaline"] > player["statmax"]["adrenaline"]:
            player["stats"]["adrenaline"] = player["statmax"]["adrenaline"]
        player["stats"]["sleepiness"] = player["stats"]["sleepiness"] - 15
        if player["stats"]["sleepiness"] < 0:
            player["stats"]["sleepiness"] = 0
        del player["inventory"][item]

    elif item == "candy bag":
        player["stats"]["memory"] = player["stats"]["memory"] + 3
        if player["stats"]["memory"] > player["statmax"]["memory"]:
            player["stats"]["memory"] = player["statmax"]["memory"]
        del player["inventory"][item]

    elif item == "burrito":
        player["stats"]["adrenaline"] = player["stats"]["adrenaline"] + 4
        if player["stats"]["adrenaline"] > player["statmax"]["adrenaline"]:
            player["stats"]["adrenaline"] = player["statmax"]["adrenaline"]
        player["stats"]["sleepiness"] = player["stats"]["sleepiness"] - 7
        if player["stats"]["sleepiness"] < 0:
            player["stats"]["sleepiness"] = 0
        del player["inventory"][item]

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
        del player["inventory"][item]
            
    elif item == "big rock":
        player["stats"]["lucidity"] = player["stats"]["lucidity"] - 20
        if player["stats"]["lucidity"] < 0:
            player["stats"]["lucidity"] = 0
        del player["inventory"][item]

    elif item == "frying pan":
        player["stats"]["social battery"] = player["stats"]["social battery"] + 5
        if player["stats"]["social battery"] < player["statmax"]["social battery"]:
            player["stats"]["social battery"] = player["statmax"]["social battery"]
        del player["inventory"][item]
    elif item == "PSPC":
        player["stats"]["social battery"] = player["stats"]["social battery"] + 5
        if player["stats"]["social battery"] < player["statmax"]["social battery"]:
            player["stats"]["social battery"] = player["statmax"]["social battery"]
        del player["inventory"][item]
    
    return player

def RW_skills(queleft, player):
    # ADD FLAVOR TEXT!!!!!!
    count = 1
    for specskill in player["skills"].keys():
        print(f"{count}) {specskill} : {player["skills"][specskill]}")
        count += 1

    while True:
        sklcho = input(f"What skill would you like to choose? 1~{count-1}:\n")
        try:
            sklcho = int(sklcho)
            if sklcho in range(1, count):
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
    if "sleepiness" in player["stats"]:
        player["stats"]["sleepiness"] = 0
    return player

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