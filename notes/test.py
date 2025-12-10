# FB 1st codespace stuff
import time as t

dictname = {"imbeded dictionary":{"key":"value", "otherkey":"other value", 10:953}}

x = list(dictname["imbeded dictionary"].keys())

count = 1
def imbededdictsundoer(diction):
    for specitem in dictname["imbeded dictionary"].keys():
        print(f"{count}) {specitem} : {dictname["imbeded dictionary"][specitem]}")
    
    dictname["imbeded dictionary"][specitem] = funcex(int(dictname["imbeded dictionary"][specitem]))[1]
    print(dictname["imbeded dictionary"][specitem])

def funcex(numericalval):
    numericalval = numericalval +1
    newnum = functex(numericalval)
    return newnum, numericalval

def functex(numberval):
    numberval += 1

x = 1
print(funcex(x))


imbededdictsundoer(dictname)
















runningoutofvariablenames = (1, 2, 4, 5)

runningoutofvariablenames = int(runningoutofvariablenames[2])

print(1+runningoutofvariablenames)

testlst = [{"val":1, "thing":3, "bloop":50}, ["This is a value it costs 1 dolla", "This is a thing it costs 3 dolla", "This is a bloop it costs 50 dolla"]]

count = 0
for item in testlst[0]:
    print(f"{item}:\n{testlst[1][count]}")
    count += 1





num = 1
for i in range(num):
    print(i)

for i in range(1, 6):
    if i in range(1, 6):
        print(i)

list = [1, 6, 9, 14, 3, 6598, 1, 3, 68, 2, 268]

print(max(list))
print(min(list))
try:
    err = 3 + "5"
    print(err)
except:
    print("error occured, cont")

print("test")

print("another test")

var = 2 + 6

print(var)

print("Test x3")

# I love using this file for like, everything

# bleep boop bap

print("test")
t.sleep(1)
print("does this work and save and push??")
t.sleep(0.5)
print("I hope so!")