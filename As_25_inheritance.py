# 1. Write a python script to create a Profile class with 3 attributes (name, email, age).

class Profile:

    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

p1 = Profile("Ashok", "ashok@gmail.com", 31)
print(p1.name)
print(p1.email)
print(p1.age)

# 2. Write a python script to update the above Profile class with encapsulation.


# 3. Write a python script to update 2nd Question, change email and age to __email and __age.

class Profile:

    def __init__(self, name, email, age):
        self.name = name
        self.__email = email
        self.__age = age

p2 = Profile("Harsh", "hms@gmail.com", 32)
print(p2.name)
print(p2._Profile__email)
print(p2._Profile__age)

# 4. Write a python script to update 2nd Question, add a class variable (platform) and create a classmethod to access it.

class Profile:

    company = "TCS"

    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def get_emp_details(self):
        print(f"Name of Employee: {self.name}")
        print(f"Email of {self.name}: {self.email}")
        print(f"Age of {self.name}: {self.age}")

p3 = Profile("Makarand", "mks@gmail.com", 34)
p3.get_emp_details()

# 5. Write a python script to create a Calculator class with 2 methods for adding and subtracting 2 values.

class Calculator:

    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def add(self):
        print(f"Addition of {self.n1} and {self.n2} is: {self.n1 + self.n2}")

    def substract(self):
        print(f"Substraction of {self.n1} and {self.n2} is: {self.n1 - self.n2}")
       
c1 = Calculator(4,6)
c1.add()
c1.substract()

# 6. Write a python script to create a Calculator 2.0 class with 2 methods for multiplication and division of 2 values and inherit it from the Calculator class.

class Calculator2(Calculator):

    def multiplication(self):
        print(f"Multiplication of {self.n1} and {self.n2} is: {self.n1 * self.n2}")

    def Division(self):
        print(f"Division of {self.n1} and {self.n2} is: {self.n1 / self.n2}")

c2 = Calculator2(10,20)
c2.add()
c2.substract()
c2.multiplication()
c2.Division()

# 7. Write a python script to create a Phone class with 2 methods to print the features (calling and sms).

class Phone:

    def make_call(self):
        print("Calling ...")

    def send_sms(self):
        print("Sending SMS...")

p1 = Phone()
p1.make_call()
p1.send_sms()

# 8. Write a python script to create a SmartPhone class by inheriting Calculator 2.0 and Phone Class.

class SmartPhone(Calculator2, Phone):
    print("In SmartPhone...")

s1 = SmartPhone(12,24)
s1.add()
s1.substract()
s1.multiplication()
s1.Division()
s1.make_call()
s1.send_sms()

# 9. Write a python script to create an application like Truecaller where names and numbers are stored. 
# Truecaller class will have 2 methods (1st to fetch the name of a number and 2nd to add a new entry).

class Truecaller:

    data = {'Ashok':9595959595, 'Harsh': 992992211, 'Mak': 9850509090}

    def __init__(self, number, name=None):
        self.number = number
        self.name = name

    def fetch_name(self):
        for name, num in self.data.items():
            if num == self.number:
                print(name)
                break

    def add_name(self):
        self.data.update({self.name:self.number})

t1 = Truecaller(9595959595)
t1.fetch_name()
t2 = Truecaller( 9970809099, 'Sahil')
t2.add_name()
print(f"Updated Dictionary: {t2.data}")

# 10. Write a python script to add the new method in SmartPhone class which accepts
# Truecaller object as a parameter and call the fetch method of Truecaller.

class SmartPhone(Calculator2, Phone):
    
    def get_name(self, truecaller_object):
        truecaller_object.fetch_name()

s2.get_name(t1)
s2 = SmartPhone(12,24)