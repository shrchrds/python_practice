# 1. Write a python script to take your name as input from the user and then print it.
name = input("Enter your name: ")
print(name)

# 2. Write a python script to take input from the user. Input must be a number.
num = int(input("Enter a number: "))
print(num)

# 3. Write a python script which takes two numbers from the user, then calculate their sum and display the result.
num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
print(f"Sum of {num1} and {num2} is: {num1+num2}")

# 4. Write a python script which takes the radius from the user and display area of a circle.
import math
radius = float(input("Enter a radius of circle: "))
area = math.pi * radius * radius
print(f"Area of circle is: {round(area,2)} square units")

# 5. Write a python script to calculate the square of a number. Number is entered by the user
num = int(input("Enter a number: "))
print(f"Square of a number {num} is: {num ** 2}")

# 6. Write a python script to calculate the area of Triangle. Number is entered by the user.
base = float(input("Enter a base of triangle: "))
height = float(input("Enter a height of triangle: "))
area = 1/2 * base * height
print(f"Area of Triangle having base {base} and height {height} is: {round(area,2)} square units")

# 7. Write a python script to calculate average of three numbers, entered by the user
num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
num3 = int(input("Enter number3: "))
average = (num1 + num2 + num3)/3
print(f"Average of numbers {num1}, {num2}, {num3} is: {average}")

# 8. Write a python script to calculate simple interest
principal = int(input("Enter principal amount in rupees: "))
rate_of_interest = float(input("Enter yearly rate of interest in %: "))
time = int(input("Enter duration in years: "))
simple_interest = principal * rate_of_interest * time / 100
print(f"Simple interest for Principal {principal} rupees, rate of interest of {rate_of_interest} % for {time} years duration is: {simple_interest} rupees")

# 9. Write a python script to calculate the volume of a cuboid.
length = float(input("Enter a length of cuboid: "))
width = float(input("Enter a width of cuboid: "))
height = float(input("Enter a height of cuboid: "))
volume = length * width * height
print(f"Volume of cuboid for length {length}, width {width}, height {height} is: {volume} cubic units")

# 10. Write a python script to calculate area of a rectangle
length = float(input("Enter a length of rectangle: "))
width = float(input("Enter a width of rectangle: "))
area = length * width
print(f"Area of rectangle for length {length}, width {width} is: {area} square units")