# 1. Write a python script to remove the last digit from a given number. (for example, if user enters 2534 then your output should be 253)
num = int(input("Enter a number: "))
new_num = int(str(num)[:-1])
print(f"New number after removing last digit from number {num} is: {new_num}")

# 2. Write a python script to get the last digit from a given number. (for example, if user enters 2089 then your output should be 9)
num = int(input("Enter a number: "))
last_num = int(str(num)[-1:])
print(f"last digit from number {num} is: {last_num}")

# 3. Write a python script to swap data of two variables
name = input("Enter a Name: ")
sirname = input("Enter Sirname: ")
name, sirname = sirname, name
print(f"modified data after swapping is: name= {name}, sirname = {sirname}")

# 4. Write a python script to find x power y, where values of x and y are given by user
x = float(input("Enter a number: "))
y = float(input("Enter a power number: "))
print(f"{x} raised to {y} is: {x**y}")

# 5. Write a python script which takes a three digit number from the user and displays only its first digit.
num = int(input("Enter a 3 digit number: "))
first_num = int(str(num)[0])
print(f"First digit from number {num} is: {first_num}")

# 6. Write a python script which takes a three digit number from the user and displays only its middle digit.
num = int(input("Enter a 3 digit number: "))
mid_num = int(str(num)[1:-1])
print(f"Middle digit from number {num} is: {mid_num}")

# 7. Write a python script which takes a three digit number from the user and displays only its last digit.
num = int(input("Enter a 3 digit number: "))
last_num = int(str(num)[-1])
print(f"Last digit from number {num} is: {last_num}")

# 8. Write a python script to use IN operator to display the data present in the list
lst = list(range(1,11))
1 in lst

# 9. Write a python script to use NOT IN operator to display the data not present in list
lst = list(range(1,11))
10 not in lst

# 10. Write a python script to use IS operator to display if both variables are the same object or not?
a = int(input("Enter a number1: "))
b = int(input("Enter a number2"))
a is b