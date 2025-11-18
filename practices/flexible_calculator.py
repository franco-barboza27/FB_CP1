# FB 1st Flexible calculator

import statistics as s
import time as t
import random as r
import math as m

print("Hello, this is a simple calculator that can give you the Sum, Average, Max, Min and Product of any numbers you enter.")
operation = input("Which would you like to do?\n1) Sum Calculator\n2) Average Calculator\n3)Maximums Calculator\n4) Minumums Calculator")

def calc(action, *nums):
    if action == "1":
        total = 0
        for num in nums:
            try:
                total += num
            except:
                continue
        return f"The sum is: {total}"
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

        return f"The average is: {avg}"
    elif action == "3":
        return f"The maximum value is: {max(nums)}"