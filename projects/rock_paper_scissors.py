# FB rock paper scissors, advanced

import random as rand
import time as t

newline_workaround = { 
"moai_thing" : ["                    ", "                    ", "                    ", "                    ", "                    ", "            _____   ", "          /- -   |  ", "         /___    |  ", "           _/     \\ ", "          |--     | ", "          |       \\ ", "          |________\\"],

"paper_parts" : ["                    ", "                    ", "                    ", "                    ", "                    ", "           ________ ", "          |--------|", "          |--------|", "          |--------|", "          |--------|", "          |--------|", "          ╵────────╵"],

"scissor_parts" : ["                       ", "                       ", "             /|  |\\    ", "            | |  | |   ", "            | |  | |   ", "            | \\  / |   ", "           /   /\\   \\  ", "           \\___\\/___/  ", "           //  ||  \\\\  ", "          ||   ||   || ", "          \\\\___||___// ", "           \\________/  "],


"dead_moai" : ["                    ", "                    ", "                    ", "                    ", "                    ", "            _____   ", "          /X X   |  ", "         /___    |  ", "           _/     \\ ", "          | 0     | ", "          |       \\ ", "          |________\\"],

"dead_paper" : ["                      ", "                      ", "                      ", "                      ", "                      ", "           ____//____ ", "          |----\\\\----|", "          |----//----|", "          |----\\\\----|", "          |----//----|", "          |----\\\\----|", "          ╵────//────╵"],

"dead_scissors" : ["                 |       ", "             /|  |  |\\   ", "            | |  |  | |  ", "            | |  |  | |  ", "            | \\  |  / |  ", "           /   / | \\   \\ ", "           \\___\\ | /___/ ", "           //  | | |  \\\\ ", "          ||   | | |   ||", "          \\\\___| | |___//", "           \\____ | ____/ ", "                 |       "],

"v.s." : ["                                               ", "                                               ", "                                               ", "                                               ", "                                               ", "          __          __       _________       ", "         | |         | |      |    _____|      ", "         \\ \\        / /       |   |____        ", "          \\ \\      / /        |____    |       ", "           \\ \\    / /          ____|   |       ", "            \\ \\__/ /    __    |        |    __ ", "            ╵──────╵   |__|   ╵────────╵   |__|"],

"you_lose" : ["                                                  ", "                                                  ", "                                                  ", "                                                  ", "                                                  ", "                                                  ", " __     __           _      ____   _____ ______ _ ", " \ \   / /          | |    / __ \ / ____|  ____| |", "  \ \_/ /__  _   _  | |   | |  | | (___ | |__  | |", "   \   / _ \| | | | | |   | |  | |\___ \|  __| | |", "    | | (_) | |_| | | |___| |__| |____) | |____|_|", "    |_|\___/ \__,_| |______\____/|_____/|______(_)"],

"you_win" : ["                                                ", "                                                ", "                                                ", "                                                ", "                                                ", "                                                ", " __     __          __          _______ _   _ _ ", " \ \   / /          \ \        / /_   _| \ | | |", "  \ \_/ /__  _   _   \ \  /\  / /  | | |  \| | |", "   \   / _ \| | | |   \ \/  \/ /   | | | . ` | |", "    | | (_) | |_| |    \  /\  /   _| |_| |\  |_|", "    |_|\___/ \__,_|     \/  \/   |_____|_| \_(_)"],

"you_tie" : ["                                                   ", "                                                   ", "                                                   ", "                                                   ", "                                                   ", "                                                   ", " __     __           _______ _____ ______ _____  _ ", " \ \   / /          |__   __|_   _|  ____|  __ \| |", "  \ \_/ /__  _   _     | |    | | | |__  | |  | | |", "   \   / _ \| | | |    | |    | | |  __| | |  | | |", "    | | (_) | |_| |    | |   _| |_| |____| |__| |_|", "    |_|\___/ \__,_|    |_|  |_____|______|_____/(_)"]
}

end = ""
index = 0
p_str = ""
while True:
    

    if end == False:
       break
    

    print("Hello! This is a rock paper scissors game!\nYou will play against a simple CPU that just randomly chooses inputs! Type 'STOP' to STOP the program.")

    cpu_points = 0
    user_points = 0

    while True:
        user_play = input(f"Rock, Paper, Scissors, SHOOT! R/P/S\n")

        comp_shoot = rand.randint (1,3)

        if user_play == "STOP":
           print("Ok, bye!")
           end = False
           break

        elif user_play == "R" and comp_shoot == 1:
            
            while index < len(newline_workaround["moai_thing"]):
              print(newline_workaround["moai_thing"][index] + "   " + newline_workaround["v.s."][index] + "   " + newline_workaround["moai_thing"][index])
              index += 1
            
            print(p_str)

            t.sleep(1)

            index = 0
            p_str = ""

            while index < len(newline_workaround["you_tie"]):
              print(newline_workaround["moai_thing"][index] + "   " + newline_workaround["you_tie"][index])
              index += 1
            
            print(p_str)

            index = 0
            p_str = ""
            



        elif user_play == "P" and comp_shoot == 2:
            while index < len(newline_workaround["paper_parts"]):
              print(newline_workaround["paper_parts"][index] + "   " + newline_workaround["v.s."][index] + "   " + newline_workaround["paper_parts"][index])
              index += 1
            
            print(p_str)

            t.sleep(1)

            index = 0
            p_str = ""

            while index < len(newline_workaround["you_tie"]):
              print(newline_workaround["paper_parts"][index] + "   " + newline_workaround["you_tie"][index])
              index += 1
            
            print(p_str)

            index = 0
            p_str = ""




        elif user_play == "S" and comp_shoot == 3:
            while index < len(newline_workaround["scissor_parts"]):
              print(newline_workaround["scissor_parts"][index] + "   " + newline_workaround["v.s."][index] + "   " + newline_workaround["scissor_parts"][index])
              index += 1
            
            print(p_str)

            t.sleep(1)

            index = 0
            p_str = ""

            while index < len(newline_workaround["you_tie"]):
              print(newline_workaround["scissor_parts"][index] + "   " + newline_workaround["you_tie"][index])
              index += 1
            
            print(p_str)

            index = 0
            p_str = ""




        elif user_play == "R" and comp_shoot == 2:
            while index < len(newline_workaround["moai_thing"]):
              print(newline_workaround["moai_thing"][index] + "   " + newline_workaround["v.s."][index] + "   " + newline_workaround["paper_parts"][index])
              index += 1
            
            print(p_str)

            t.sleep(1)

            index = 0
            p_str = ""

            while index < len(newline_workaround["you_lose"]):
              print(newline_workaround["dead_moai"][index] + "   " + newline_workaround["you_lose"][index])
              index += 1
            
            print(p_str)

            index = 0
            p_str = ""
            cpu_points += 1

            print(f"You have {user_points}")
            print(f"The computer has {cpu_points}")




        elif user_play == "P" and comp_shoot == 3:
            while index < len(newline_workaround["paper_parts"]):
              print(newline_workaround["paper_parts"][index] + "   " + newline_workaround["v.s."][index] + "   " + newline_workaround["scissor_parts"][index])
              index += 1
            
            print(p_str)

            t.sleep(1)

            index = 0
            p_str = ""

            while index < len(newline_workaround["you_lose"]):
              print(newline_workaround["dead_paper"][index] + "   " + newline_workaround["you_lose"][index])
              index += 1
            
            print(p_str)
            

            index = 0
            p_str = ""
            cpu_points += 1

            print(f"You have {user_points}")
            print(f"The computer has {cpu_points}")




        elif user_play == "S" and comp_shoot == 1:
            while index < len(newline_workaround["scissor_parts"]):
              print(newline_workaround["scissor_parts"][index] + "   " + newline_workaround["v.s."][index] + "   " + newline_workaround["moai_thing"][index])
              index += 1
            
            print(p_str)

            t.sleep(1)

            index = 0
            p_str = ""

            while index < len(newline_workaround["you_lose"]):
              print(newline_workaround["dead_scissors"][index] + "   " + newline_workaround["you_lose"][index])
              index += 1
            
            print(p_str)

            index = 0
            p_str = ""
            cpu_points += 1

            print(f"You have {user_points}")
            print(f"The computer has {cpu_points}")




        elif user_play == "R" and comp_shoot == 3:
            while index < len(newline_workaround["moai_thing"]):
              print(newline_workaround["moai_thing"][index] + "   " + newline_workaround["v.s."][index] + "   " + newline_workaround["scissor_parts"][index])
              index += 1
            
            print(p_str)

            t.sleep(1)

            index = 0
            p_str = ""

            while index < len(newline_workaround["you_win"]):
              print(newline_workaround["moai_thing"][index] + "   " + newline_workaround["you_win"][index])
              index += 1
            
            print(p_str)

            index = 0
            p_str = ""
            user_points += 1

            print(f"You have {user_points}")
            print(f"The computer has {cpu_points}")




        elif user_play == "P" and comp_shoot == 1:
            while index < len(newline_workaround["paper_parts"]):
              print(newline_workaround["paper_parts"][index] + "   " + newline_workaround["v.s."][index] + "   " + newline_workaround["moai_thing"][index])
              index += 1
            
            print(p_str)

            t.sleep(1)

            index = 0
            p_str = ""

            while index < len(newline_workaround["you_win"]):
              print(newline_workaround["paper_parts"][index] + "   " + newline_workaround["you_win"][index])
              index += 1
            
            print(p_str)
            

            index = 0
            p_str = ""
            user_points += 1

            print(f"You have {user_points}")
            print(f"The computer has {cpu_points}")




        elif user_play == "S" and comp_shoot == 2:
            while index < len(newline_workaround["scissor_parts"]):
              print(newline_workaround["scissor_parts"][index] + "   " + newline_workaround["v.s."][index] + "   " + newline_workaround["paper_parts"][index])
              index += 1
            
            print(p_str)

            t.sleep(1)

            index = 0
            p_str = ""

            while index < len(newline_workaround["you_win"]):
              print(newline_workaround["scissor_parts"][index] + "   " + newline_workaround["you_win"][index])
              index += 1
            
            print(p_str)

            index = 0
            p_str = ""
            user_points += 1

            print(f"You have {user_points}")
            print(f"The computer has {cpu_points}")





        else:
            print("\nSorry but your input did not match the desired format ;-;\n\n")
        





        if cpu_points == 10:
            print("\nSeems like the computer won! \nBetter luck next time! \n\n")
            cpu_points = 0
            user_points = 0

            break
        elif user_points == 10:
            print("\nIt seems like you won! Good job!\n\n")
            cpu_points = 0
            user_points = 0

            break