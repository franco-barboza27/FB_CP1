# FB Multiplication table assignment 

print("Hello, this is a multiplication table! If things go accordingly, you will even be able to choose how big it is!")

table = []

while True:
    size = int(input("How big do you want your multiplication table to be?:"))
    multi = 1
    
    for row in range(1, size+1):
        table.clear()

        for num in range(1, size+1):
            table.append(multi * num)
        multi += 1
        print(*table)