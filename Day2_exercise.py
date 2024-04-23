name = input("What is your first name? ")
last_name = input("What is your last name? ")
if (len(name) + len(last_name) < 12):
    print(f'{name} {last_name} is shorter than the average American name')
elif (len(name) + len(last_name) == 12):
    print(f'{name} {last_name} is exact average American name')
else:
    print(f'{name} {last_name} is longer than the average American name')

