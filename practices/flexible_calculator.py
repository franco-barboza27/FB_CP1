# FB 1st Flexible calculator
import math as m

def calc(action, *numeros):
    # convert my tuple of user inputs into a list
    nums = []
    untupleator = list(numeros)
    unfilterednums = untupleator[0]
    # then filter that list by making a new one with only integer versions of the items
    for num in unfilterednums:
        try:
            num = int(num)
            nums.append(num)
        except:
            continue
    # calculates the sum of all items in the list by looping over it and using addition
    if action == "1":
        total = 0
        for num in nums:
            try:
                total += num
            except:
                continue
        print(f"The sum is: {total}")
    # similar to sum, however it divides by the amount of things in the list at the end
    elif action == "2":
        total = 0
        numamount = 0
        for num in nums:
            try:
                numamount += 1
                total += num
            except:
                continue
        avg = total/numamount
        print(f"The average is: {avg}")
    # use methods to get the max, min, or product
    elif action == "3":
        print(f"The maximum value is: {max(nums)}")
    elif action == "4":
        print(f"The minimum value is: {min(nums)}")
    elif action == "5":
        print(f"The product of that is {m.prod(nums)}")
# presents the program, allows for multiple uses, and stupid proofs the menu selection
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
        calc(operation, numbers)
    else:
        print("That is not an option...\nI feel like 'option' is not the correct way to spell it...")
