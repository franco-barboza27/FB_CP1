# FB 1st Idiot proof avanced

print("Hello, this program will ask you for your full name, your phone number and your GPA.")
print("We will now begin.")

while True:
    first_name = input("What is your first name?")
    last_name = input("What is your last name?")

    if first_name.isalpha() and last_name.isalpha():
        first_name.strip(" ")
        last_name.strip(" ")
        first_name.capitalize()
        last_name.capitalize()
        print("Hello" + first_name + " " + last_name)
        break
    else:
        print("Please try that again. Without numbers or characters.")

while True:
    digits = input("What is your phone number?")
    digits_len = len(digits)
    digits.strip(" ")

    if digits.isdigit() and digits_len == 9: