# FB 1st What is My Grade

print("Hello this is a letter grade calculator")

grade_storage = {}
stop = True

while True:

    stop_check = input("Input STOP to STOP the program.:\n")

    if stop_check == "STOP":
        "Bye"
        exit
    else:
        print("Ok, moving on.")

    while True:
        cur_class = input("What class do you want to calculate for?:\n")

        if cur_class == "STOP":
            print("Ok bye")
            exit
        else:
            print("Thanks.")

        grade = float(input(f"What is your grade in {cur_class} (input as #.#)?:\n"))

        if grade >= 93:
            print("Your grade is an A. Exceeding most expectations.")
        elif grade >= 90:
            print("Your grade is an A-")
        elif grade >= 87:
            print("Your grade is a B+. Definitely above average.")
        elif grade >= 83:
            print("Your grade is an B")
        elif grade >= 80:
            print("Your grade is a B-. Above average... ish")
        elif grade >= 77:
            print("Your grade is an C+. A teeny bit above average.")
        elif grade >= 73:
            print("Your grade is a C")
        elif grade >= 70:
            print("Your grade is a C-")
        elif grade >= 67:
            print("Your grade is an D+. You are below average, in general.")
        elif grade >= 63:
            print("Your grade is a D. You are even more below average than a D+.")
        elif grade >= 60:
            print("Your grade is an D-. Wow... why is your grade so low?????")
        elif grade <= 59.99:
            print("Your grade IS AN F. Do better or I SWEAR I'll send you to the factories of the great depression if you don't bring those grades up by next semester!")
        else:
            print("Your inputted a letter or something. I LITERALLY told you what I wanted... TSK TSK... wait that's actually impossible because if you input something that's not a number it gives you an error instead.")

            grade_storage.update({cur_class : grade})
        
        cur_grade_total = sum(grade_storage.values())

        grade_avg = cur_grade_total / (len(grade_storage) + 1)

        print(f"Your current average grade is {grade_avg}%")