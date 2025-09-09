# FB 1st Simple Calculator advanced

# make intro
# make loop
# make input vars
# make output options

print("Hello, this is a very simple calculator that only works with integers, please avoid using it for math class.")

while True:

    frst_num = int(input("What is the first number that you want to use?:\n"))

    scnd_num = int(input("What is the second number you want to use?:\n"))

    operation = input("What is the operation you would like to do?\nAddition (+) subtraction (-) multiplication (*) division (/) integer division (//) and modulo division (%) and exponents (**): \n")

    if operation == "+":
        print(f"{frst_num} + {scnd_num} = {frst_num + scnd_num}")
    elif operation == "-":
        print(f"{frst_num} - {scnd_num} = {frst_num - scnd_num}")
    elif operation == "*":
        print(f"{frst_num} * {scnd_num} = {frst_num * scnd_num}")
    elif operation == "/":
        print(f"{frst_num} / {scnd_num} = {frst_num / scnd_num}")
    elif operation == "//":
        print(f"{frst_num} // {scnd_num} = {frst_num // scnd_num}")
    elif operation == "%":
        print(f"{frst_num} % {scnd_num} = {frst_num % scnd_num}")
    elif operation == "**":
        print(f"{frst_num} ** {scnd_num} = {frst_num ** scnd_num}")
    else:
        print("I'm sorry, your operation input did NOT match the required format, please repeat.")