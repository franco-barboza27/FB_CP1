# FB 1st letter grade

#make

print("Hello this is a letter grade calculator")

grade_storage = {}

while stop:

    stop_check = input("Input STOP to STOP the program.")
    stop = True

    if stop_check == "STOP":
        print("Oh... ok. Goodbye!")
        stop = False
    else:
        print("Ok, moving on.")

    while stop:
        grade = float(input("What is your grade in one of your classes (input as a decimal)?:\n"))

        if grade >= 93:
            print("Your grade is an A. Exceeding most expectations.")
        elif grade >= 90 and grade <= 92.99:
            print("Your grade is an A-")
        elif grade >= 87 and grade <= 89.99:
            print("Your grade is a B+. Definitely above average.")
        elif grade >= 83 and grade <= 86.99:
            print("Your grade is an B")
        elif grade >= 80 and grade <= 82.99:
            print("Your grade is a B-. Above average... ish")
        elif grade >= 77 and grade <= 79.99:
            print("Your grade is an C+. A teeny bit above average.")
        elif grade >= 73 and grade <= 76.99:
            print("Your grade is a C")
        elif grade >= 70 and grade <= 72.99:
            print("Your grade is a C-")
        elif grade >= 67 and grade <= 69.99:
            print("Your grade is an D+. You are below average, in general.")
        elif grade >= 63 and grade <= 66.99:
            print("Your grade is a D. You are even more below average than a D+.")
        elif grade >= 60 and grade <= 62.99:
            print("Your grade is an D-. Wow... why is your grade so low?????")
        elif grade <= 59.99:
            print("Your grade IS AN F. Do better I SWEAR I'll send you to the factories of the great depression if you don't bring those grades up by next semester!")
        else:
            print("Your grade is somehow in the inbetween that my if statements didn't cover.")