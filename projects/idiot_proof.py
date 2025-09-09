# FB 1st Idiot proof advanced

print("Hello, this program will ask you for your full name, your phone number and your GPA.")
print("Also this one is minimal because I don't have the time to make it better.")
print("We will now begin.")


def askSystem():
    while True:
        first_name = input("What is your first name?\n")
        last_name = input("What is your last name?\n")

        if first_name.isalpha() and last_name.isalpha():
            print("Hello " + first_name.strip(" ").capitalize() + " " + last_name.strip(" ").capitalize())
            break
        else:
            print("Please try that again. Without numbers or special characters.\n")

    while True:
        digits = input("What is your phone number?\n")

        if digits.isdigit() and len(digits) == 10:
            
            first_part = digits.strip()[:3]
            scnd_part = digits.strip()[3:6]
            thrd_part = digits.strip()[6:]

            print("OK, I'll text you later, " + first_part + " " + scnd_part + " " + thrd_part)
            break
        else:
            print("Please try that again. Without letters or special characters.\n")

    while True:
        gpa = float(input("What is your GPA? P.S, don't use special characters OR letters or it WILL break.\n"))

        if gpa > 4:
            print("Please try that again. Without letters or special characters and in standard, unweighted GPA form.\n")
        else:
            print("Wow,")
            print(gpa)
            print("is really good!")
            break
askSystem()

print("Thanks for completing this.")