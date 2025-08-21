#FB 1st seasons starter
#make a program that asks a favorite season

lastName = print("What is your last name?: \n")
favSeason = input("Cool, what is your favorite season? Fa/Su/Wi/Sp: \n")

if favSeason == "Fa":
    print(f"Oh really? I like fall too {lastName}, it's probably not my fave but its better than SUMMER")
elif favSeason == "Su":
    print(f"Oh wow... I kinda dont like the summer, or winter really but I GUESS it's ok that you do. {lastName}")
elif favSeason == "Wi":
    print(f"I kinda HATE winter, {lastName} it's only saving grace is Christmas.")
elif favSeason == "Sp":
    print(f"Wow! {lastName} That's my favorite too!!!!!!")
else:
    print("sorry but that input doesn't match the required format")