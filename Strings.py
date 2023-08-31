from typing import Match


name = "Kanye West is the goat"

# length of the string

print(len(name))

# slicing 0 ---> 3 last will not be included

print(name[0:4])

# interpreted as len(name) -3 : len(name) - 1

print(name[-3:-1])

print(name.split(" "))

# count the occurence

print(name.count("Kanye"))

# print(name.index("Jay-z"))

# many other functions

# if else

a = 17

if a > 18:
    print("You can do it")
else:
    print("You cannot do it")


# match

x = 4

match x:
    case 0:
        print("Zero")

    case 4:
        print("Four")

    case 5:
        print("Five")

    case _:
        print("Dammm")
