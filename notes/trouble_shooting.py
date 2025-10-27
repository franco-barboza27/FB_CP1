# FB personal trouble shooting file because I forgot to commit and push from home so now I can't make actual changes to the file I was working on withoug breaking my tree :(
import time
import random
sentence = {
    
    "word_one" : ["t", "h", "i", "s", " "],
    "word_two" : ["w", "o", "r", "k", "s"]

            }
var = ""
index = 0


x = [1, 2, 3, 4, 5, 6, 7]
print(x)

y = list(x)
print(y)


enemystats = {"Health":100, "Defence":100}
player_stats = {"Health":100, "Defence":50, "Attack":150}

damage = ((player_stats["Attack"] - enemystats["Defence"]) // 1)

if damage < 0:
    damage = damage*0

print(damage)



while index < len(sentence["word_one"]):
    print(sentence["word_one"][index] + "   " + sentence["word_two"][index])
    index += 1




while True:
    print(random.randint(1, 2))
    time.sleep(.05)
    break


print("Starting process...", flush=True)
time.sleep(1) # Simulate some work
print("Process complete.", flush=True)

num = 1

string = "Hello"

print(f"{string} --- {num}")