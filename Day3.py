print("################## Functions ##################")


# def func_name(argument=default_param):
#   func body
#   return x

# default param always after required
def greet(person, msg="Hi", greet="Nice to meet you"):
    print(f"{msg} {person}, \n{greet}")


# Named args - keyword args
greet("Ann", greet="See you soon")

# SCOPE - scope boundary where it cam be used depends on where they are initially defined
# LEGB - lexical enclosing global build-in
# Lexical-Local - inside the function and accessed by that func
# enclosing - nested func - inner functions has access to outer vars
# global - var outside the functions (all funcs have access to them
# build in - pre-defined and accessed from anywhere

# "NOTE fo JAVA - functions when assign! don't rewrite values of the var with the same name!"
temp = -3


def getting_warmer():
    # print(temp+2) - true- we have access to global param but not to reassign them
    # global temp # --- to reassign temp use
    temp = 13


getting_warmer()
print(temp)

print("################## LISTS ##################")
# ordered collections of values
# list = [val1, val2,val3]
# list()
# list("hello") - [h,e,l,l,o]
# list(range(3)
# to access - list_name[index]
# to add
my_list = list(range(3))  # 1,2,3
my_list.append(4)  # add to the end

my_list.extend("abs")  # a,b,c - also great to add another list
print(my_list)
# insert(index, element)
my_list.insert(len(my_list), 5)
print(my_list)
# slice
# list[start:stop:step]
# clear() - empty the list
my_list.clear()
my_list.extend([1, 2, 3])
my_list[1:3] = [4, 5, 6, 7]  # take second and third and replace
print(my_list)
# remove('first value to remove') o_o
# pop() - remove last and return it pop(2) - third element
print(my_list.pop())
print(my_list)
# del list_name[index]
# del list_name[2:]
del my_list[0]
for element in my_list:
    print(element)

# Nested Lists
stuff = ["string", True, None]
stuff.append(my_list)
print(stuff)
# access to nested lists
print(stuff[3][2])
del stuff[3]
print(stuff + [1, 2])
print(stuff * 2)

# methods
my_list.reverse()
print(my_list)
print(str(my_list.count(5)) + " time 5 was found in my_list")
my_list.sort()

print("################## Lists are mutable ##################")
list_my = my_list
# if we change one the other will change as well as it refer to the same container
print(list_my)
my_list.append(1)
print(my_list)
print(list_my)
a = 4
b = a
a += 5
print(a, b)
#copy() list (shallow) or usr : (slice)
l2 = my_list.copy()
#deepcopy() - make a copy of the list and any nested objects


print("################## Compare lists ##################")
print(my_list == list_my)  # to compare contents inside of the lists
print(my_list is list_my)  # to compare the identity (same container)
new_list = [4, 5, 6, 1]
print(new_list == list_my)  # to compare contents inside of the lists
print(new_list is list_my)  # to compare the identity (same container)

print("################## Split & Join ##################")
# split is a string method that will split a string on a given char (delimiter) - return a list
birthday = "11/06/1991"
print(birthday.split("/"))
# join - str method that joins together itarable elements into a single str.
# using called str as a separator
full_name = ["Sherr", "Nika", "Evgenyevna"]
print(" ".join(full_name))

print("################## List Unpacking ##################")
# val from list to vars
# exact numbers or * - for remaining
day, month, year = birthday.split("/")
print(year)
