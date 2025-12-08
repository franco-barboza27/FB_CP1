import time, sys, random

def startup_room():
    tun = [5, 10, ["sample 1", "sample 2", "sample 3", "sample 4", "sample 5"]]
    nan = [5, 50, ["sample 1", "sample 2", "sample 3", "sample 4", "sample 5"]]

    wrldr = 0

    print("You should wake up!\n No! You should keep sleeping, just a bit longer!")

    if wrldr is False:
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

        winlossrw = tun_fight(player)
    elif wrldr == "2":
        player = {"state":{"alive":True},
                  "stats":{"lucidity":0, "social energy":10, "charm":10, "imagination":0},
                  "statmax":{"lucidity":50, "social energy":10},
                  "inventory":{},
                  "Collected items":{},
                  "usable items":{"Sleep tea":"decreases lucidity by 10", "Big rock":"-20 lucidity",
                                  "energy drink":"gives you 2 adrenaline and -15 sleepiness", "candy bag":"gives you 3 memory", "burrito":"decreases sleep by 10 and increases adrenaline by 3"},
                  "skills":{},
                  "unacquired skills":{"Random recollection":"costs 5 adrenaline, you do 10 questions", "Save the hardest for last":"costs 2 adrenaline, you do 4 questions", "Guess":"costs 2 adrenaline, answer 2 questions, don't gain sleep."},
                  }
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

def RW_items():
    pass

def DW_items():
    pass

def RW_skills():
    pass

def DW_skills():
    pass

def tun_fight():
    pass

def math_t():
    pass

def chem_t():
    pass

def history_t():
    pass

def nan_fight():
    pass

def combat():
    pass

def cont():
    pass

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