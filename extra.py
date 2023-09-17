x = [1, 2, 3, 4]

print(dir(x))

# print(help(str))

# Dunder

class Emp:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"The name of the emp is {self.name}"


e = Emp("Chad")
print(str(e))


# Method  Overriding 


# Defining parent class
class Parent():
	
	# Constructor
	def __init__(self):
		self.value = "Inside Parent"
		
	# Parent's show method
	def show(self):
		print(self.value)
		
# Defining child class
class Child(Parent):
	
	# Constructor
	def __init__(self):
		self.value = "Inside Child"
		
	# Child's show method
	def show(self):
		print(self.value)
		
		
# Driver's code
obj1 = Parent()
obj2 = Child()

obj1.show()
obj2.show()



# Operator Overloading 

print(1 + 2)

# concatenate two strings
print("Geeks"+"For")

# Product two numbers
print(3 * 4)

# Repeat the String
print("Geeks"*4)

