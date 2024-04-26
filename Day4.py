print("################## Dictionaries ##################")
# key-value pairs
movie = {
    "title": "Amadeus",
    "imdb": 8.3,
    "runtime": "3h",
    "year": 2002
}
print(f'the type of movie var {type(movie)}')
print(f'check if key rating is in dictionary "Movie": {"rating" in movie}')
# access
print(movie["title"])
print(movie.get("rating"))
print(movie.get("runtime"))
# add item
movie["rating"] = "R"

print("################## Merging Dictionaries ##################")
# merging dictionary - update()
# dict1.update(dict2)
# ** - combine in a new
dict1 = {"a": 3, "b": 2}
dict2 = {"c": 3, "d": 4, "a": 1}
dict3 = {**dict1, **dict2}
print(dict3)
# new that is used
# UNION V3
dict4 = dict1 | dict2
print(dict4)
print("################## Iterate Dictionaries ##################")

# iterating through the dict
# keys() values() items()

movie_list = list(movie.items())
print(type(movie_list[0]))

for key in movie.keys():
    print(f'key "{key}" - value "{movie[key]}"')

print("################## items() ##################")
for k, v in movie.items():
    print(f'key "{k}" - value "{v}"')

print(f"function pop() is removing element and return it's value {movie.pop("imdb")}")
print(f'function popitem() is removing last added key-value pair and return it {movie.popitem()}')
# del dict_name[key]
# dict_name.clear()


print("""

################## Tuples are immutable ##################""")
# immutable, ordered
# tuple_name = ("item",true, [list items])
one_item_tpl = "first",  # tuple with one item
tuple_name = ("str", 34, [1, 4])
print(tuple_name[:])  # slice
print(tuple_name[2])  # access
# tuple_name[1]=34 - TypeError: 'tuple' object does not support item assignment
tuple_name[2].append(8)
print(tuple_name)
print("""

################## Set ##################""")
# unique, unordered, all elements are immutable
set_name = {1, 2, 3, "fff", True}
print(type(set_name))
print("################## add item ##################")
set_name.add(5)
# set_name[2] - error


for items in set_name:
    print(items)

print("################## remove / discard ##################")
set_name.remove(2)
set_name.discard(3)
set_name.remove(True)
# set_name.remove(4) - will cause an error
#clear()SS
print(f'after remove: {set_name}')
set_name1 = {1, 2, 5, ("fff", True)}
print('another set with tuple:')
for items in set_name1:
    print(items)
set_name1.remove(("fff", True))
print("################## Intersection/Union/Difference ##################")
# Intersection - returns new set of common items
print(set_name & set_name1)
# Union - returns new set of all unique items
print(set_name | set_name1)
# Difference - returns new set with elements from left and not right
print(set_name-set_name1) # unique for set_name
print(set_name1.difference(set_name))
