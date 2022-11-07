# 1. Write a python program to create a user class with 3 properties : name, age, email.

class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

u = User("Shivanand", 33, "sne@gmail.com")
print(u.name)
print(u.age)
print(u.email)

# 2. Write a python program to create a user class with a method to greet the user.

class User:
    def __init__(self, name):
        self.name = name

    def greet_user(self):
        print(f"Hello, {self.name}")

u1 = User("Shivanand")
u1.greet_user()

# 3. Write a python program to create 2 objects of the user class and assign different values.

class User:
    def __init__(self, name):
        self.name = name

    def greet_user(self):
        print(f"Hello, {self.name}")

u1 = User("Shivanand")
u1.greet_user()

u2 = User("Sunny")
u2.greet_user()

# 4. Write a python program to init default values for user object using __init__ method.

class User:
    def __init__(self, name="Shivanand", age=33, email="sne@gmai.com"):
        self.name = name
        self.age = age
        self.email = email

u3 = User()
print(u3.name)
print(u3.age)
print(u3.email)

# 5. Write a python program to delete the age property of the user.

del u3.age
print("Successfully Deleted")


# 6. Write a python program to create 3 user objects and find the youngest of all.

class User3:
    def __init__(self, name1, name2, name3):
        self.name1 = name1
        self.name2 = name2
        self.name3 = name3

    def youngest(self):
        return min(self.name1, self.name2, self.name3)

us3 = User3("Naveen", "Saurabh", "Sudhanshu")
print(us3.youngest())

# 7. Write a python program to create a Laptop class with 4 attributes (brand, ram, cpu, hdd) and 2 methods (showConfig() to print the values, __init__() to initialize the values).

class Laptop:

    def __init__(self, brand, ram, cpu, hdd):
        self.brand = brand
        self.ram = ram
        self.cpu = cpu
        self.hdd = hdd

    def showConfig(self):
        print("Brand of Laptop: ",self.brand)
        print("Ram of Laptop: ", self.ram)
        print("CPU of Laptop: ", self.cpu)
        print("HDD of Laptop: ", self.hdd)

l1 = Laptop("HP", 16, "i7", "1 TB")
l1.showConfig()

# 8. WRT 7th Question, create  3 Laptop objects and add them to the list in the sorted  order based on the ram size.

l1 = Laptop("HP", 16, "i7", "1 TB")
l2 = Laptop("Dell", 8, "i5", "512 GB")
l3 = Laptop("Asus", 4, "i3", "256 GB")
rams = []
rams.append(l1.ram)
rams.append(l2.ram)
rams.append(l3.ram)
print(sorted(rams))

# 9. Write a python program to create a School class and 3 instance variables and 1 class variable.

class School:

    name = "SM Vidyalaya"

    def __init__(self, standard, division, roll_number):
        self.standard = standard
        self.division = division
        self.roll_number = roll_number

s = School(9, "A", 10)
print(f"Class Variable: {s.name}")
print(f"Instance Variable 1: {s.standard}")
print(f"Instance Variable 2: {s.division}")
print(f"Instance Variable 3: {s.roll_number}")


# 10. Define a class Employee with instance object variables empid, name, salary. Write __init__() method in the class to initialize instance object variables. 
# Also define instance methods to input fields and display field values.

class Employee:

    def __init__(self, empid, name, salary):
        self.empid = empid
        self.name = name
        self.salary = salary

    def employee_details(self):
        print(f"EmployeeID: {self.empid}")
        print(f"Name of Employee: {self.name}")
        print(f"Salary of Employee: {self.salary}")

e1 = Employee(100, "Sada", 10000)
e2 = Employee(101, "Mahadu", 12000)
e1.employee_details()
e2.employee_details()