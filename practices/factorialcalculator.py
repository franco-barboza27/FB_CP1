# FB 1st Factorial Calculator

# def multiply(a, b):
    # returnn a*b
def multiply(a, b):
    return a*b
# if __name__ = __main__":
# this gives an error that main isn't defined
if __name__ == "__main__":

    # while true: int(
                # V
    while True:
        try:
        # try:
            user_inp = input("This is a factorial calculator, please input a whole number:\n")
            user_inp = int(user_inp)
            # ^ the comparisons later on were breaking because of this not being an int yet
            # user_inp = input(instructions))  
                                # ^ I took the artistic liberty of making new ones
            if user_inp < 0:
                print("Invalid")
            # if user_inp < 0:
                #print(invalid)
            if user_inp == 0:
                print("0! is equal to 1")
                break
            # if user inp == 0:
                # print(goodbye)
                # brake
                # ^ Actually this always equals one so instead I'll print "1"
            else:
                num = 1
                total = 0
                for x in range(1, user_inp+1):
                    num = multiply(num, x)
                total = num
                print(f"{user_inp}! is equal to {num}")
            # else: 
                # num = 1
                # for x in range(user_inp)
                    # num = multiply(num, x)
                # print(f{user_inp}!={num})
        except:
            print("Error occured, did you make sure it was a WHOLE number greater than zero, and had:\nNO spaces, special characters OR letters?")
        # except:
            # print("error occured try again")