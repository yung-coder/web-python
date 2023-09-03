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
