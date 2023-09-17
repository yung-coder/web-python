class Person:
    name = "Saksham"
    gender = "Male"
    worth = 90

    def info(self):
        print(f"{self.name} is a {self.gender}")


a = Person()
print(a.gender)
a.info()


# Constructor


class Car:
    def __init__(self, Name, Model):
        print(f"it is {Name} of Modal {Model}")


b = Car("Cruze", "2010")


# Decorartors


def greet(fx):
    def mfx():
        print("Yo")
        fx()
        print("Bye")

    return mfx


@greet
def hello():
    print("Lets go")


hello()


# Getters and Settters


class MyClass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

    # Getter

    @property
    def ten_value(self):
        return 10 * self._value

    # Setter

    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value / 10


obj = MyClass(10)
print(obj.ten_value)
obj.show()


# Inheritance


class Worker:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def show(self):
        print(f"Id is {self.id} is {self.name}")


class Coder(Worker):
    def showLang(self):
        print("The Default language is Js")


c = Coder("Saksham", 47)
c.show()
c.showLang()


# Instance vs Class variables


class Demo:
    companyName = "Appl"  # class variables

    def __init__(self):
        self.salary = 67

    def show(self):
        print(f"Hmm {self.salary}")


emp1 = Demo()
emp1.companyName = "New"


# Super Keyword


class Emp:
    def __init__(self, id, name, Add):
        self.id = id
        self.name = name
        self.Add = Add


# Class freelancer inherits EMP
class Freelance(Emp):
    def __init__(self, id, name, Add, Emails):
        super().__init__(id, name, Add)
        self.Emails = Emails


Emp_1 = Freelance(103, "Suraj kr gupta", "Noida", "KKK@gmails")
print("The ID is:", Emp_1.id)
print("The Name is:", Emp_1.name)
print("The Address is:", Emp_1.Add)
print("The Emails is:", Emp_1.Emails)
