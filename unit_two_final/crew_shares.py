# FB 1st crew shares project

# make a variable for the total money CHECK
# make a story CHECK
# make a variable for the leftover money divided by the total shares CHECK
# make a variable for the total money given to the captain, the first mate and the crewmates CHECK

print("This is a mini story about pirates who get money, also sorry about your story teller this time.\nThis one has amnesia or something.")

print("HEY! Rude... ANYWAYS...")

while True:
    print("Once upon a time, there was a ship and it's crew...")

    inp_count = 0

    crew_mates = int(input("How many crew mates are there, not including the first mate and captain? It's a little bit fuzzy for me... \nEnter Answer: \n"))

    tot_money = 0
    min_money = crew_mates * 500 + 10 + crew_mates


    while True:
        if inp_count == 0:
            tot_money = float(input("How much money did they make again???? I forgot. \nEnter Answer: \n"))
            inp_count += 1
        elif tot_money >= min_money:
            print(f"Oh that's right, they had {tot_money:.2f}")
            print(f"It's coming back to me now.\nThe captain got 7 shares, the first mate got 3 shares and the crew each got 1 share of the money, aside from the 500 they each got")
            break
        else:
            print("Sorry, but that doesn't sound quite about right... I think it might be a bit more...")
            tot_money = float(input("How much money did they ACTUALLY make? \nEnter Answer: \n"))

    crew_start = 500 * crew_mates
    leftover = tot_money - crew_start

    share = leftover / (crew_mates + 10)

    capt_mon = share * 7
    frst_mon = share * 3
    crew_mon = share * crew_mates + crew_start

    print(f"One share for the crew was something like... {share:.2f}$?")
    print(f"So the captain got {capt_mon:.2f}$ and the first mate got {frst_mon:.2f}$")
    print(f"Each crewmate got one share and 500 dollars for a total of... let me do the math... {crew_mon}$")


