# FB Multiplication table assignment 

print("Hello, this is a multiplication table! If things go accordingly, you will even be able to choose how big it is!")



len_table = []
multi_table = []

table = [
        len_table,
        multi_table
        ]

len_size = 0
tall_size = 0


while True:
    size = int(input("How big do you want your multiplication table to be?:"))
    
    for num in len_table:
        len_size += 1
        len_table.append(len_size)

        for mult in len_table:
            multi_table.append(len_size * num)