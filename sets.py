# String fromatting
# f-string

name = "Chad"
country = "India"


print(f"Hey my name is {name} and I am from {country}")


# docstring


def square(n):
    """Takes in a number n, returns the square of n"""
    print(n**2)


square(5)
print(square.__doc__)

# sets

info = {"jack", 14, 5, 19}
print(info)

for i in info:
    print(i)


# sets function

s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}
print(s1.intersection(s2))
print(s1.union(s2))

# Dictionaries

dic = {"Chad": "Loser", "Car": "Lucid"}

print(dic.keys())
