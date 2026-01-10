numlist = [1, 9, 3, 10, 5, 12, 4, 7, 11, 6, 8 ,2]

count = 0
for num in numlist:
    count += 1
    num -= numlist[count]
    print(num)
    if num < 0:
        num += 12
    elif num > 12:
        num -= 12
    print(num)