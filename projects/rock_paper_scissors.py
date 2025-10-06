# FB rock paper scissors, advanced

rock_sym = """
            _____
          /- -   |
         /___    |
           _/     \\
          |--     |
          |_______|       
"""

paper_sym = """
           _____
          |-----|
          |-----|
          |-----|
          ╵─────╵
"""

scissors_sym = """
            /|  |\\
           | |  | |
           | |  | |
           | |  | |
           \\__/\\__/
            /  |  \\
           |   |   |
           \\___|___/
"""

r = "Rock"
p = "Paper"
s = "Scissors"

while True:
    print("Hello! This is a rock paper scissors game!\nYou will play against a simple CPU that just randomly chooses inputs!")
    player = input(f"Do you want to do {r}(R), {p}(P) or {s}(S)?\n {rock_sym}     {paper_sym}   {scissors_sym}")