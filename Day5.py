print("################## Functions ##################")
# min/max
list = [2, 4, 1, 7, 33, -5]
print(min(list))

print("################## * and ** ##################")


# how to write function that takes any numbers of args - use a star!
def average(*args):
    total = 0
    for arg in args:
        total += arg
    return total / len(args)


print(average(1, 4, 6, 8))


# no need to pass anything in *
def login(first, *args):
    print("does nothing")


login("charlie")


# ** is for ant number of keyword args (kwargs)
# dictionary of key - value pairs

def demo(**kwargs):
    print(kwargs)


demo(color="red", car="Ferrari")

def add_twice(num, lst=[]):
    lst.append(num)
    lst.append(num)
    print(lst)