# FB Multiplication table assignment 

print("Hello, this is a multiplication table! If things go accordingly, you will even be able to choose how big it is!")

table = []
cur_num = 0
size = input(print("How big do you want your multiplication table to be?"))

while enumerate(table) < size:
    cur_num += 1
    table.append(cur_num)