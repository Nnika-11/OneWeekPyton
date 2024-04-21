print("################## Methods ##################")

# methods are functouns that are part of the objects
# obj.method()
from random import randint

myStr = "string"
print(myStr.capitalize())
print(myStr.upper())
print(myStr)  # it wasnt changed

# Functions signatures - what functions expect of
# str.strip([chars]) [] - optional
print("    hello\n".strip())
print("----h-e-l-l-o.... . .-.. .-.. ---".strip("-. "))
print("----h-e-l-l-o means.... . .-.. .-.. ---".lstrip("-. "))

# Replace - str.replace(old, new, [count])
apples = '5lb apples'
oranges = '7lb oranges'
print((apples + " and " + oranges).replace('lb', 'kg'))

# method chaining
print("verOnikA.is@the.best".strip().lower())

print("######################### Conditionals ###############################")

# if condition:
#   indentation and code
# elif condition:
#   another code
# else:
#   code if everything else is false


print("throw a coin")
result = randint(0, 1)
if result == 0:
    print("Heads!")
else:
    print("Tails!")

print("####################### LOOP ################################")
# while condition:
#   will run untill condition true

# for item in iterable:
#   statement

# for num in range (start, stop, step):
#   print(num)
# start included stop is not, start by default 0
for num in range(1, 6):
    print(num, end=" ")

# break, continue
print()
# diceroller
dice_num = int(input("How many dice are we rolling? "))
sides_num = int(input("How many sides on each die? "))

while 1:
    result = ""
    for num in range(dice_num):
        roll = randint(1, sides_num)
        result += str(roll) + "|"
    print(result)
    stop_it = input("Roll again? ('q' to quit) ")
    if stop_it.lower() == "q":
        break
