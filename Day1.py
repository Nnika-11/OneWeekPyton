print("################## Python variables & Operators ##################")

# Python Simple Types:
# Integer (int)
# multi assignment
a, b, c = 123578, 0, -44
print(type(a))
# Float (float)
fl1, fl2, fl3 = 3.555, 0.01, 1.5e+0
print(type(fl3))

# Operators
print(33 / 5)
# floor division - integer division
print(33 // 5)
# Exponentiation
print(5 ** 3)
# Assignment Operator
b += 5
print(b)

# NoneType - null
nothing = None
print(type(nothing))

# String (str)
hen = "hen"
print(type(hen))
print(len(hen))
hen += "\nis cute"
print(hen)
print(hen[:3])
print(hen[4:-5])
print(hen[::2])  # step

# casting
print(type(str(fl1)))
print((int(-8.9)))

# write input for asking an age in years to print it out in days
a = float(input("How old are you? "))
print("you are " + str(a * 365) + " days old")
# f strings - treats {code running first}
print(f"you are {a * 365} days old")

# boolean - bool
print(type(True))
print(type('true'))
# operators: >= ,  ==, != , in (member of sequence)
print(4.00001 == 4)
print(4.0000 == 4)
print(bool(None))  # False

# more advanced
print('w' > 'a')  # true
print('aaa' < 'AAA')  # false
# python stores strings in order - check by ord(car)
print(f"{ord('w')} is 'w' order compared with {ord('a')} the order of 'a' and {ord('A')} the order of 'A'")