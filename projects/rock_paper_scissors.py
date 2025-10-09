# FB rock paper scissors, advanced
import random as rand


rock_ref = """
            _____
          /X X   |
         /___    |
           _/     \\
          |--     |
          |       \\
          |________\\
"""

paper_ref = """
           ________
          |--------|
          |--------|
          |--------|
          |--------|
          |--------|
          ╵────────╵
"""

scissors_ref = """
                 | 
             /|  |  |\\
            | |  |  | |
            | |  |  | |
            | \\  |  / |
           /   / | \\   \\
           \\___\\ | /___/
           //  | | |  \\\\
          ||   | | |   ||
          \\\\___| | |___//
           \\____ | ____/
                 |
"""
vs_ref = """
             __          __       _________
            | |         | |      |    _____|
            \\ \\        / /       |   |____
             \\ \\      / /        |____    |
              \\ \\    / /          ____|   |
               \\ \\__/ /    __    |        |    __
               ╵──────╵   |__|   ╵────────╵   |__|
"""

you_win = """
__     __          __          _______ _   _ _ 
\ \   / /          \ \        / /_   _| \ | | |
 \ \_/ /__  _   _   \ \  /\  / /  | | |  \| | |
  \   / _ \| | | |   \ \/  \/ /   | | | . ` | |
   | | (_) | |_| |    \  /\  /   _| |_| |\  |_|
   |_|\___/ \__,_|     \/  \/   |_____|_| \_(_)
"""

you_lose = """
 __     __           _      ____   _____ ______ _ 
 \ \   / /          | |    / __ \ / ____|  ____| |
  \ \_/ /__  _   _  | |   | |  | | (___ | |__  | |
   \   / _ \| | | | | |   | |  | |\___ \|  __| | |
    | | (_) | |_| | | |___| |__| |____) | |____|_|
    |_|\___/ \__,_| |______\____/|_____/|______(_)
"""
print(you_win)
print(you_lose)


newline_workaround = { 
"moai_thing" : ["\n", "\n", "\n", "\n", "            _____", "\n          /- -   |", "\n         /___    |", "\n           _/     \\", "\n          |--     |", "\n          |       \\", "\n          |________\\"], 
"paper_parts" : ["\n", "\n", "\n", "\n", "________", "\n          |--------|", "\n          |--------|", "\n          |--------|", "\n          |--------|", "\n          |--------|", "\n          ╵────────╵"],
"scissor_parts" : ["/|  |\\", "\n          | |  | |", "\n          | |  | |", "\n           | \\  / |", "\n          /   /\\   \\", "\n           \\___\\/___/", "\n           //  ||  \\\\", "\          ||   ||   ||", "\n          \\\\___||___//", "\n           \\________/"],

"dead_moai" : ["            _____", "\n          /X X   |", "\n         /___    |", "\n           _/     \\", "\n          | 0     |", "\n          |       \\", "\n          |________\\"],
"dead_paper" : ["____//____", "\n          |----\\\\----|", "\n          |----//----|", "\n          |----\\\\----|", "\n          |----//----|", "\n          |----\\\\----|", "\n          ╵────//────╵"],
"dead_scissors" : ["                 |", "             /|  |  |\\", "            | |  |  | |", "            | |  |  | |", "            | \\  |  / |", "           /   / | \\   \\", "           \\___\\ | /___/", "           //  | | |  \\\\", "          ||   | | |   ||", "          \\\\___| | |___//", "           \\____ | ____/", "                 |"],

"you_lose" : [" __     __           _      ____   _____ ______ _ ", " \ \   / /          | |    / __ \ / ____|  ____| |", "  \ \_/ /__  _   _  | |   | |  | | (___ | |__  | |", "   \   / _ \| | | | | |   | |  | |\___ \|  __| | |", "    | | (_) | |_| | | |___| |__| |____) | |____|_|", "    |_|\___/ \__,_| |______\____/|_____/|______(_)"],
"you_win" : [" __     __          __          _______ _   _ _ ", " \ \   / /          \ \        / /_   _| \ | | |", "  \ \_/ /__  _   _   \ \  /\  / /  | | |  \| | |", "   \   / _ \| | | |   \ \/  \/ /   | | | . ` | |", "    | | (_) | |_| |    \  /\  /   _| |_| |\  |_|", "    |_|\___/ \__,_|     \/  \/   |_____|_| \_(_)"]
}

r = "Rock"
p = "Paper"
s = "Scissors"

while True:
    print("Hello! This is a rock paper scissors game!\nYou will play against a simple CPU that just randomly chooses inputs!")

    cpu_points = 0
    user_points = 0

    while True:
        user_play = input(f"Rock, Paper, Scissors, SHOOT! R/P/S\n")

        comp_shoot = rand.randint (1,3)

        if user_play == "R" and comp_shoot == 1:
            print("\nThe computer played Rock! You Tied!\n\n")
        elif user_play == "P" and comp_shoot == 2:
            print("\nThe computer played Paper! You Tied!\n\n")
        elif user_play == "S" and comp_shoot == 3:
            print("\nThe computer played Scissors! You Tied!\n\n")
        elif user_play == "R" and comp_shoot == 2:
            print("\nThe computer played Paper! You Lost")
            cpu_points += 1
        elif user_play == "P" and comp_shoot == 3:
            print("\nThe computer played Scissors! You Lost!\n\n")
            cpu_points += 1
        elif user_play == "S" and comp_shoot == 1:
            print("\nThe computer played Rock! You Lost!\n\n")
            cpu_points += 1
        elif user_play == "R" and comp_shoot == 3:
            print("\nThe computer played Scissors! You Won!\n\n")
            user_points += 1
        elif user_play == "P" and comp_shoot == 1:
            print("\nThe computer played Rock! You Won!\n\n")
            user_points += 1
        elif user_play == "S" and comp_shoot == 2:
            print("\nThe computer played Paper! You Won!\n\n")
        else:
            print("\nSorry but your input did not match the desired format ;-;\n\n")
        
        if cpu_points == 10:
            print("\nSeems like the computer won! \nBetter luck next time! \n\n")
            cpu_points = 0
            user_points = 0
        elif user_points == 10:
            print("\nIt seems like you won! Good job!\n\n")
            cpu_points = 0
            user_points = 0