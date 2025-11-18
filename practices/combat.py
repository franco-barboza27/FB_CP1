# FB 1st Combat program

import random
import time
import sys

def dialog(text, txtspd, delay=.05):
    a = ""
    delay = 0

    if txtspd == "S":
        delay = .1
    elif txtspd == "M":
        delay = .05
    elif txtspd == "F":
        delay = .025
    elif txtspd == "admin":
        delay = .001
    else:
        delay = .05

    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)

    return a

def stats_shower(stats):
    display = ""

    for desc, val in stats.items():
        display += f"{desc} --- {val} \n"
    
    return display





def player_choice(playerstats, enemystats):

    if playerstats["Health"] < 0:
        dialog("You Died! This is a roguelike, so back to the start you go!\n", txt_spd)
        sys.exit()

    dialog("It's your turn now!\nTry using your basic attack on the enemy\n", txt_spd)

    while True:
        options = input(dialog("1) Attack\n2) Skills\n3) Bestiary\nEnter:", txt_spd))
        while True:
            if options == "1":
                player_turn(playerstats, enemystats)
                break
            elif options == "2":
                dialog("But don't you want to use an attack first? Also that's a work in progress! You can't use it yet :(\n", txt_spd)
                break
            elif options == "3":
                dialog("I would, but I don't know anything about my enemies yet.\n", txt_spd)
                break
            else:
                dialog("That's not an option!\n", txt_spd)
                break






# The game will temporarilly be a roguelike 
def player_turn(playerstats, enemystats):

    listenemy = list(enemystats.keys())
    listplyr = list(playerstats.keys())
    enemy = listenemy[0]


    if playerstats["Health"] < 0:
        dialog("You Died! This is a roguelike, so back to the start you go!\n", txt_spd)
        sys.exit()
    else:
        dialog(f"You attack the {enemy}!\n", txt_spd)

    damage = ((playerstats["Attack"] - enemystats["Defence"]) // 1)

    if damage < 0:
        damage = 0

    if listplyr[0] == "Mage":
        dialog(f"You sent out an orb of basic mana, simple but efficient-it uses no mental energy!\nIt did {damage} damage!\n", txt_spd)
        enemystats["Health"] -= damage
    elif listplyr[0] == "Fighter":
        dialog(f"You use your BIG strong MUSCLES and puch it in the face!\nYou did {damage} damage!\n", txt_spd)
        enemystats["Health"] -= damage
    elif listplyr[0] == "Rogue":
        dialog(f"You throw a dagger at the enemy, stabbing it for {damage} damage.\n", txt_spd)
        enemystats["Health"] -= damage
    elif listplyr[0] == "Admin":
        dialog(f"You did {damage} damage.\n", txt_spd)
        enemystats["Health"] -= damage

    enemy_turn(enemystats, playerstats)




def enemy_turn(enemystats, playerstats):

    listenemy = list(enemystats.keys())
    listplyr = list(playerstats.keys())
    enemy = listenemy[0]

    dialog(f"You have {playerstats["Health"]} HP.\n", txt_spd)
    if enemystats["Health"] >= 0:
        dialog(f"The enemy has {enemystats["Health"]} HP.\n", txt_spd)
    else:
        enemystats["Health"] = 0
        dialog(f"The enemy has {enemystats["Health"]} HP.\n", txt_spd)

    if enemystats["Health"] <= 0:
        fight_result = dialog("You beat the Wild bat!\nAnd with that, your adventure is over!\n", txt_spd)
        sys.exit()
    else:
        dialog(f"The {enemy} attacks you!\n", txt_spd)

    damage = ((enemystats["Attack"] - playerstats["Defence"]) // 1)

    if damage < 0:
        damage = damage*0

    enemy_attack = random.randint(1,2)

    if listenemy[0] == "Wild bat":
        if enemy_attack == 1:
            dialog(f"The Wild bat barrels through the air at you!\nIt did {damage} damage!\n", txt_spd)
            playerstats["Health"] -= damage
        elif enemy_attack == 2:
            dialog(f"The Wild bat claws at your general direction!\nIt did {damage} damage!\n", txt_spd)
            playerstats["Health"] -= damage

    player_choice(playerstats, enemystats)





def turn_choice(player_spd, enemy_spd, player_stats, enemy_stats):

    choice = 0
    # Use for loop to iterate over the list that enemytypes gives
    if player_spd == enemy_spd:
        choice = random.randint(1, 2)
        if choice == 1:
            player_choice(player_stats, enemy_stats)
        else:
            enemy_turn(enemy_stats, player_stats)

    elif player_spd < enemy_spd:
        enemy_turn(enemy_stats, player_stats)
    else:
        player_choice(player_stats, enemy_stats)





def enemyrand(enemytypes, enemy_bank):
    "PLACEHOLDER --- WIP"
    # when it gets the amount of enemies,
    # and then selects that amount randomly from the given bank, 
    # order them using their mons_types[enemyindex]["Speed"] from most speed to least speed, and send that list to the turn choice function
    amount = enemy_bank

    for amount in enemy_bank:

        enemy_amount = 0

        if amount > 3:
            enemy_amount = random.randint(1,4)
            amount -= enemy_amount
        elif enemy_bank <=3:
            enemy_amount = random.randint(1, enemy_bank+1)
            amount -= enemy_amount

# I need to figure out a good place to store skills for both players and enemies
# I also need to figure out a way to decide what skills an enemy will use, will it be random? or will they have patterns for the user to use?>
# I could do both, for example maybe regular enemies could have randomized turn usage, and bosses could be more choreographed

def player_skills(playerstats, playerskills, enemystats):
    "PLACEHOLDER --- WIP"

def enemy_skills(enemystats, enemyskills, playerstats):
    "PLACEHOLDER --- WIP"

# I also need to figure out where to store the players classes because I want them to have different level up rates 
# but also I want it to get harder to level up with more levels
# Furthermore I need to decide what the rate of increase will be for the exp requirement to level up,
# and how to store what level they are,
# then unlock more skills based on their stored level

def leveling(exprate, expdrop, currentlvl):
    "PLACEHOLDER --- WIP"

while True:

    player_stats = {}

    character_types = [{"Mage":"A magic user who relies on mental fortitude(MF) to use spells.", "Health":50, "Attack":20, "Defence":10, "Mental Energy":30, "Speed":30, "EXP rate":1.2, "Base Accuracy":1},
                {"Fighter":"A fighter who uses physical prowess to pummel enemies.", "Health":100, "Attack":30, "Defence":30, "Mental Energy":10, "Speed":25, "EXP rate":1.2, "Base Accuracy":1},
                {"Rogue":"A speedy scout with all around moderate stats", "Health":75, "Attack":20, "Defence":20, "Mental Energy":20, "Speed":40, "EXP rate":1.2, "Base Accuracy":1},
                {"Admin":"Used by the creator to test the game, if you're using it, I hope you're also testing the game.", "Health":10, "Attack":100000, "Defence":1, "Mental Energy":100000, "Speed":10, "EXP rate":100000, "Base accuracy":100000}]

    mons_types = [{"Wild bat":"A large bat whose claws won't hesitate to gouge you eyes out, be careful!", "Health":40, "Attack":20, "Defence":5, "Mental Energy":0, "Speed":35, "EXP":10, "Base Accuracy":1},
                {"Giant centipede":"Disgusting. A hundred legs comes with quite some speed and it's tough exoskeleton makes it a formidable foe.", "Health":40, "Attack":10, "Defence":30, "Speed":30, "EXP":20, "Base Accuracy":1},
                {"Fire sprite":"A fist sized ball of fire with a equally petulant behavior, watch for it's potent magic!", "Health":20, "Attack":30, "Defence":10, "Speed":30, "EXP":15, "Base Accuracy":.7},
                {"Living Flame":"A coalition of fire sprites working together as one. It is much stronger in all aspects, maybe try disrupting their unison?", "Health":30, "Attack":40, "Defence":15, "Speed":20, "EXP":30, "Base Accuracy":.9},
                {"Fuoco, the igneous":"A mass of rocks manipulated by a Greater Fire Sprite. It uses the rocks as a home of sorts, but it also uses it to squish trespassers. It might be a good idea to attack when you can see it's core!", "Health":80, "Attack":40, "Defence":50, "Speed":20, "EXP":500, "Base Accuracy":.8}]



    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    dialog("Greetings, this is a simple RPG type game. To begin, I would like to ask a few questions.\n", "M")
    while True:
        txt_spd = input(dialog("What speed of dialog would you like? The current one, Medium(M), Fast(F) or Slow(S)?\nEnter:", "M"))

        if txt_spd == "M":
            dialog("Very well\n", txt_spd)
        elif txt_spd == "F":
            dialog("Very well\n", txt_spd)
        elif txt_spd == "S":
            dialog("Very well\n", txt_spd)
        elif txt_spd == "admin":
            dialog("Very well\n", txt_spd)
        else:
            dialog("I'm sorry, that input did not match the format.\n", txt_spd)
            continue

        dia_check = input(dialog("Is this speed sufficient?\nY/N Enter:", txt_spd))

        if dia_check == "Y":
            dialog("Very well, we will now continue\n", txt_spd)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            break
        elif dia_check == "N":
            dialog("Very well, you may now choose again.\n", txt_spd)
        else:
            dialog("I'm sorry, but that is not in the required format.\n", txt_spd)

    dialog("You find yourself in a dark cave.\nYour head is pounding as if you got hit in the head by a club.\n'Where am I?'\n'It hurts to even think right now...'\nSuddenly, you hear a sound, getting louder and louder.\nIt sounds like wings flapping in the air, and soon, you feel the gusts of wind on your neck.\n'Who is that?!' You say, running forward, and spinning around.\nIt takes a second for your eyes to adjust, but in the nick of time, you see a gigantic bat hurtling towards you.\nYou dodge out of the way, surprised by your own reflexes.\n'Come on, think! Me, THINK!'\nYou try to remember, what did you do before being here, in this... cave?\n", txt_spd)

    dialog("Remember.... you were a mage? No a fighter?... Maybe some sort of Rogue?\n", txt_spd)

    while True:

        career = input(dialog("1) Mage\n2) Fighter\n3) Rogue\nEnter:", txt_spd))
        career_index = 0
        print("\n")

        if career == "1":
            dialog(stats_shower(character_types[0]), txt_spd)
            player_stats = character_types[0]
            career_index = 0
            career = "Mage"
        elif career == "2":
            dialog(stats_shower(character_types[1]), txt_spd)
            player_stats = character_types[1]
            career_index = 1
            career = "Fighter"
        elif career == "3":
            dialog(stats_shower(character_types[2]), txt_spd)
            career_index = 2
            player_stats = character_types[2]
            career = "Rogue"
        elif career == "admin":
            dialog(stats_shower(character_types[3]), txt_spd)
            career_index = 3
            player_stats = character_types[3]
            career = "Admin"
            dialog("Oh I didn't know you knew about this!\nHello, creator... or someone who actually looked through the code...", txt_spd)
        else:
            dialog("That did not match the required input.", txt_spd)

        stat_conf = input(dialog("\nAre you sure you're remembering correctly?\nEnter(Y/N):", txt_spd))

        if stat_conf == "Y":
            break
        elif stat_conf == "N":
            dialog("'Hmm... No... think HARDER you HAVE to remember, or you're SCREWED!'\n", txt_spd)
        else:
            dialog("'That's not relevant right now!'\n", txt_spd)

    dialog(f"'That's right! I was a {career}'\n", txt_spd)



    # level 1 and tutorial loop, only has bats, and currently only 1 fight
    # In the finished version will have a minimum of 3 to beat level, with a max of 8 and then forced to move on

    while True:
        dialog("Suddenly, you remember how to fight--slightly--you remember your basics.\n", txt_spd)
                                                            # Eventually this function call should hopefully be using the enemy randomizer instead of 0
        turn_choice(character_types[career_index]["Speed"], mons_types[0]["Speed"], character_types[career_index], mons_types[0])

# Future thing's to add in the case I continue this project
    #
    #
    #
        # each level will have a bank of enemies to choose from randomly, and when the initial bank is filled/used(gauranteed encounters), it goes to the next bank(optional encounters/ encounters at specific parts/100% random but still required encounters)
        # randomized amounts per wave of enemies will be selected, in a range of 1-3(depending on level difficulty) at once and if there's 3 or less enemies left in the bank, it's a range of 1-enemies_in_bank+1
    #
    #
    #
        # Make a level difficulty stat for each level that basically just decides how hard the level should be
        # (which will decide things like, max amount of concurrent enemys you might fight)

        # level 2 bats and centipedes, random selection, but the first time is always a bat and the next is always a centipede
        # level 3 fire sprites start appearing and theres also some centipedes
        # level 4 mix of fire sprites and centies, one living flame at the end
        # level 5 2 living flames and the boss
    #
    #
    #
        # Make a functional inventory/loot/collectibles system that remembers items and things like that
    #
    #
    #
        # Add a way for the bestiary to keep track of how many times the player has killed an enemy, and only unlock the entry AFTER they get that many kills 
        # (I might make it a drop thing, like the enemy drops a piece of info in whatever form, or the user finds the description/buys it)
    #
    #
    #
        # PLACEHOLDER FOR FUTURE IDEAS