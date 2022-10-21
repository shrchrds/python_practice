# 1. Write a python script to display the number of days in a given month number.

month = int(input("Enter the month value in numeric format: "))
if month in (1,3,5,7,8,10,12):
    print(f"There are 31 days in month {month} ")
elif month == 2:
    print(f"There are 28 days in month {month}")
else:
    print(f"There are 30 days in month {month}")

# 2. Write a menu driven program to perform following operations - Addition, Subtraction, Multiplication, Division

num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
menu = int(input("1: for Addition, \n2: for Substraction, \n3: for Multiplication and\n4: for Division: "))

if menu == 1:
    print(f"Addition of {num1} and {num2} is: {num1 + num2}")
elif menu == 2:
    print(f"Substraction of {num1} and {num2} is: {num1 - num2}")
elif menu == 3:
    print(f"Multiplication of {num1} and {num2} is: {num1 * num2}")
else:
    print(f"Division of {num1} and {num2} is: {num1 / num2}")

# 3. Write a menu driven program with the following options:
# a. Check whether a given set of three numbers are lengths of an isosceles
# triangle or not
# b. Check whether a given set of three numbers are lengths of sides of a right
# angled triangle or not
# c. Check whether a given set of three numbers are equilateral triangle or not
# d. Exit.

num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
num3 = int(input("Enter number3: "))

menu = input("""Enter from following:
                a: To check whether a given set of three numbers are lengths of an isosceles, 
                b: To check whether a given set of three numbers are lengths of sides of a right angled triangle or not
                c: To check whether a given set of three numbers are equilateral triangle or not
                d: exit """)

if menu == 'a':
    if (num1 == num2 and num1 != num3 and num2 != num3) or (num2 == num3 and num1 != num2 and num1 != num3) or (num3 == num1 and num3 != num2 and num2 != num3) :
        print(f"{num1}, {num2}, {num3} are lengths of an isosceles triangle")
    else:
        print(f"{num1}, {num2}, {num3} are NOT lengths of an isosceles triangle")
elif menu == 'b':
    if ((num1**2 + num2**2) == num3**2) or ((num2**2 + num3**2) == num1**2) or ((num1**2 + num3**2) == num1**2):
        print(f"{num1}, {num2}, {num3} are lengths of sides of a right angled triangle")
    else:
        print(f"{num1}, {num2}, {num3} are NOT lengths of sides of a right angled triangle")
elif menu == 'c':
    if num1 == num2 and num1 == num3 and num2 == num3:
        print(f"{num1}, {num2}, {num3} are lengths of an equilateral triangle")
    else:
        print(f"{num1}, {num2}, {num3} are NOT lengths of an equilateral triangle")
elif menu == 'd':
    pass

# 4. Write a program which takes user’s age and display the category of person.
# Age below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 - Experienced, Age above or equal 60 - Senior Citizen.

age = int(input("Enter your age in years: "))
if age < 10:
    print("Kid")
elif age < 20:
    print("Teen")
elif age < 40:
    print("young")
elif age < 60:
    print("Experienced")
elif age >=60:
    print("Senior Citizen")

# 5. Write a program which takes a number from user.
# Print Saurabh Shukla if the number is even, print Prateek Jain if the number is negative odd number
# and print Aditya Choudhary if number is positive odd number.

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Saurabh Shukla")
elif num % 2 == 1 and num < 0 :
    print("Prateek Jain")
elif num % 2 == 1 and num > 0 :
    print("Aditya Choudhary")

# 6. Write a python program to check whether a given string is a multiword string or single word string using match case statement
string = input("Enter a string: ")
if len(string.split()) == 1:
    length_of_string = 1
else:
    length_of_string = 2

match length_of_string:
    case 1:
        print('single string')
    case 2:
        print('multiword string')

# 7. Write a python program to check whether a given number is positive, negative or zero using match case statement

num = int(input("Enter a number: "))
if num > 0 :
    n = 1
elif num < 0:
    n = -1
else:
    n = 0
match n:
    case 1:
        print("Positive Number")
    case -1:
        print("Negative Number")
    case 0:
        print("Zero Number")

# 8. Write a python script to check whether two given strings are identical,
# first string comes before the second in dictionary order or first string comes after the second string in dictionary order using match case statement

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
if string1 == string2:
    order = 0
elif string1 < string2:
    order = 1
else:
    order = 2
match order:
    case 0:
        print("two given strings are identical")
    case 1:
        print('first string comes before the second in dictionary order')
    case 2:
        print('first string comes after the second string in dictionary order')

# 9. Write a python script to check whether a given year is
# a. Non century leap year
# b. Century leap year
# c. Non century non leap year
# d. Century non leap year

year = int(input("Enter a year: "))

if year % 4 == 0 and year % 100 !=0:
    print("Non century leap year")
elif year % 100 == 0 and year % 400 == 0:
    print("Century leap year")
elif year % 4 != 0 and year % 100 !=0:
    print("Non century Non leap year")
elif year % 100 == 0 and year % 400 != 0:
    print("Century non leap year")

# 10. Write a program to display day name on the basis of user’s liking of a colour. Ask user for his favorite colour. User can answer in a sentence like “I like red colour”.
# Assuming all colour name entered by user is in lowercase. Use match case to display day name associated with the colour.
# a. Yellow - Monday
# b. Blue - Tuesday
# c. Orange - Wednesday
# d. White - Thursday
# e. Black - Friday
# f. Red - Saturday
# g. All other colours - Sunday

color = input('Enter your favourite color: ')
if 'yellow' in color:
    col_match = 1
elif 'blue' in color:
    col_match = 2
elif 'orange' in color:
    col_match = 3
elif 'white' in color:
    col_match = 4
elif 'black' in color:
    col_match = 5
elif 'red' in color:
    col_match = 6
else:
    col_match = 7

match col_match:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")