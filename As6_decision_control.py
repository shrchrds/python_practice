# 1. Write a python script to check whether a given number is positive or non-positive
a = int(input("Enter a number: "))
if a > 0 :
    print(f"{a} Number is a Positive Number ")
else:
    print(f"{a} Number is a Not a Positive Number ")

# 2. Write a python script to check whether a given number is divisible by 5 or not
num = int(input("Enter a number: "))
if num % 5 == 0:
    print(f"{num} Number is divisible by 5 ")
else:
    print(f"{num} Number is not divisible by 5 ")

# 3. Write a python script to check whether a given number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is an Even Number")
elif num % 2 == 1:
    print(f"{num} is an Odd Number")

# 4. Write a python script to print greater between two numbers. Print number only once even if the numbers are the same.
num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
if num1 > num2 :
    print(f"{num1} is greater than {num2}")
elif num2 > num1 :
    print(f"{num2} is greater than {num1}")
else:
    print(f"Both Numbers are same: {num1}")

# 5. Write a python script to print two given words in dictionary order
word1 = input("Enter Word1: ")
word2 = input("Enter Word2: ")
if word1 < word2:
    print(word1, word2)
else:
    print(word2,word1)

# 6. Write a python script to check whether a given number is a three digit number or not.
num = int(input("Enter a number: "))
if len(str(num)) == 3:
    print(f"{num} is a 3 digit number")
else:
    print(f"{num} is not 3 digit number")

# 7. Write a python script to check whether a given number is positive, negative or zero.

num = int(input("Enter a number: "))
if num > 0 :
    print(f"{num} is a Positive number")
elif num < 0 :
    print(f"{num} is a Negative number")
else:
    print(f"{num} is a Zero Number")

# 8. Write a python script to check whether a given quadratic equation has two real & distinct roots, real & equal roots or imaginary roots

# quadratic equation: ax^2 + bx + c = 0
# discriminant = b^2 - 4ac

a = eval(input("Enter a number coeficient of x^2: "))
b = eval(input("Enter a number coeficient of x: "))
c = eval(input("Enter a number: "))

if b**2 - 4*a*c < 0:
    print("roots are imaginary")
elif b**2 - 4*a*c > 0:
    print("roots are real & distinct")
elif b ** 2 - 4 * a * c == 0:
    print("roots are real & equal")

# 9. Write a python script to check whether a given year is a leap year or not.
year = int(input("Enter a number: "))
if year % 4 == 0 :
    print("Leap Year")
else:
    print("Not a Leap Year")

# 10. Write a python script to print greater among three numbers. Print number only once even if the numbers are the same.
num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
num3 = int(input("Enter number3: "))
if num1 > num2 and num1 > num3 :
    print(f"{num1} is greater among three numbers")
elif num2 > num1 and num2 > num3 :
    print(f"{num2} is greater among three numbers")
elif num1 == num2 and num1 == num3:
    print(f"All numbers are same")
else:
    print(f"{num3} is greater among three numbers")

# 11. Write a python script to take the month value in numeric format and display the number of days in it.

month = int(input("Enter the month value in numeric format: "))
if month in (1,3,5,7,8,10,12):
    print(f"There are 31 days in month {month} ")
elif month == 2:
    print(f"There are 28 days in month {month}")
else:
    print(f"There are 30 days in month {month}")

# 12. Write a python script to accept one complex number from the user and display the greater number between real part and imaginary part
complex_num = eval(input("Enter a complex number: "))
if complex_num.real > complex_num.imag :
    print(f"{complex_num.real} is greater number between real and imaginary part")
else:
    print(f"{complex_num.imag} is greater number between real and imaginary part")