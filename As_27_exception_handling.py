# 1. Write a python script to create a ArithmeticError
a = 5
b = int(input("Enter a number: "))

try:
    if a == b:
        raise ArithmeticError()
    c = a/b
    print(c)

except ArithmeticError:
    print("a and b should not be same")

# 2. Write a python script to create a ValueError

a = 5

try:
    b = int(input("Enter a number: "))
    if type(b) != int:
        raise ValueError()
except ValueError:
    print("Enter a number..")


# 3. Write a python script to handle the ArithmeticError

a = 5

try:
    b = int(input("Enter a number: "))
    c = a/b
    print(c)
except ArithmeticError as e:
    print(e)

# 4. Write a python script to handle a ValueError

a = 5

try:
    b = int(input("Enter a number: "))
    c = a/b
    print(c)

except ValueError:
    print("Enter a number...")

# 5. Write a python script to handle multiple Exception in one try

a = 5

try:
    b = int(input("Enter a number: "))
    c = a/b
    print(c)

except ArithmeticError:
    print("Enter non zero number...")

except ValueError:
    print("Enter a number...")

except Exception:
    print("There is some problem in code...")

# 6. Write a python script to create a calculator with 4 basic operations, and handle a maximum number of exceptions.

class Calculator:
    
    try:
        a = int(input("Enter a number1: "))
        b= int(input("Enter a number2: "))

    except ValueError:
        print("Enter number...")
    
    except Exception as e:
        print(e)
    
    def add(self):
        try:
            print(self.a + self.b)

        except AttributeError:
            print("Enter correct attribute values...")

        except Exception as e:
            print(e)

    def substract(self):
        try:
            print(self.a - self.b)
        
        except AttributeError:
            print("Enter correct attribute values...")

        except Exception as e:
            print(e)
        
    def multiplication(self):
        try:
            print(self.a * self.b)
            
        except AttributeError:
            print("Enter correct attribute values...")

        except Exception as e:
            print(e)

    def division(self):
        try:
            z = self.a/self.b
            print(z)
        except ZeroDivisionError:
            print("Enter non zero number...")
        except Exception as e:
            print(e)

c = Calculator()
c.division()

# 7. Write a python script to add a finally block for the above script


class Calculator:
    
    try:
        a = int(input("Enter a number1: "))
        b= int(input("Enter a number2: "))

    except ValueError:
        print("Enter number...")
    
    except Exception as e:
        print(e)
    
    def add(self):
        try:
            print(self.a + self.b)

        except AttributeError:
            print("Enter correct attribute values...")

        except Exception as e:
            print(e)

        finally:
            if type(self.a) and type(self.b) == int:
                print(f"Addition of {self.a} and {self.b} completed")

    def substract(self):
        try:
            print(self.a - self.b)
        
        except AttributeError:
            print("Enter correct attribute values...")

        except Exception as e:
            print(e)

        finally:
            if type(self.a) and type(self.b) == int:
                print(f"Substraction of {self.a} and {self.b} completed")
        
    def multiplication(self):
        try:
            print(self.a * self.b)
            
        except AttributeError:
            print("Enter correct attribute values...")

        except Exception as e:
            print(e)

        finally:
            if type(self.a) and type(self.b) == int:
                print(f"Multiplication of {self.a} and {self.b} completed")

    def division(self):
        try:
            z = self.a/self.b
            print(z)

        except ZeroDivisionError:
            print("Enter non zero number...")

        except Exception as e:
            print(e)

        finally:
            if type(self.a) and type(self.b) == int and self.b != 0:
                print(f"Division of {self.a} and {self.b} completed")

c = Calculator()
c.add()
c.substract()
c.multiplication()
c.division()

# 8. Write a python script to implement try except and else block for division

def division(a,b):
    try:
        z = a/b

    except ZeroDivisionError:
        print("Enter non zero number...")

    except Exception as e:
        print(e)

    else:
        print(z)
division(4,5)

# 9. Write a python script to raise a ValueError.

a = 5

try:
    b = int(input("Enter a number: "))
    if type(b) != int:
        raise ValueError()
    c = a/b
    print(c)
except ValueError:
    print("Enter a number...")

except Exception as e:
    print(e)

# 10. Write a python script to implement a nested Try Except block

try:
    a = int(input("Enter a number1: "))
    b = int(input("Enter a number2: "))

    try:
        z = a / b
    
    except ZeroDivisionError:
        print("Enter a non zero number..")

    except Exception as e:
        print(e)

    else:
        print(z)

except ValueError:
    print("Enter a number ... ")

except Exception as e:
    print(e)