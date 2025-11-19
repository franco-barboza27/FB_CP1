# FB 1st Flexible calculator
import math as m

def calc(action, *numeros):
    nums = list(numeros)
    for num in nums:
        try:
            int(num)
        except TypeError:
            continue

    if action == "1":
        total = 0
        for num in nums:
            try:
                total += num
            except TypeError:
                continue
        print(f"The sum is: {total}")
    elif action == "2":
        total = 0
        numamount = 0
        for num in nums:
            try:
                numamount += 1
                total += num
            except TypeError:
                continue
        avg = total/numamount

        print(f"The average is: {avg}")
    elif action == "3":
        max(nums)
        print(f"The maximum value is: {nums}")
    elif action == "4":
        min(nums)
        print(f"The minimum value is: {nums}")
    elif action == "5":
        m.prod(nums)
        print(f"The product of that is {nums}")

print("Hello, this is a simple calculator that can give you the Sum, Average, Max, Min and Product of any numbers you enter.")

while True:
    operation = input("Which would you like to do?\n1) Sum Calculator\n2) Average Calculator\n3) Maximums Calculator\n4) Minumums Calculator\n5) Product Calculator:\n")
    if operation.isnumeric() == False:
        print("That is not an option...")
        continue
    if int(operation) in range(1, 6):
        numbers = []
        while True:
            num = input("What number would you like to be the first number? (input STOP to STOP):\n")
            if num == "STOP":
                break
            numbers.append(num)
        print(calc(operation, numbers))
    else:
        print("That is not an option...\nI feel like 'option' is not the correct way to spell it...")
