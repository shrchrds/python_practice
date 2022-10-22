# 1. Write a python script to calculate sum of first N natural numbers
N= int(input("Enter a number to print sum of first N natural numbers: "))
sum = 0
for i in range(1,N+1):
    sum += i
print(f"Sum of first {N} natural numbers is: {sum}")

# 2. Write a python script to calculate sum of squares of first N natural numbers
N= int(input("Enter a number to print sum of squares of  first N natural numbers: "))
sum = 0
for i in range(1,N+1):
    sum += i**2
print(f"Sum of squares of first {N} natural numbers is: {sum}")

# 3. Write a python script to calculate sum of cubes of first N natural numbers
N= int(input("Enter a number to print sum of cubes of  first N natural numbers: "))
sum = 0
for i in range(1,N+1):
    sum += i**3
print(f"Sum of cubes of first {N} natural numbers is: {sum}")

# 4. Write a python script to calculate sum of first N odd natural numbers
N= int(input("Enter a number to print sum of first N odd natural numbers: "))
sum = 0
for i in range(1,N+1):
    sum += 2*i - 1
print(f"Sum of first {N} natural numbers is: {sum}")

# 5. Write a python script to calculate sum of first N even natural numbers
N= int(input("Enter a number to print sum of first N even natural numbers: "))
sum = 0
for i in range(1,N+1):
    sum += 2*i
print(f"Sum of first {N} natural numbers is: {sum}")

# 6. Write a python script to calculate factorial of a given number
fact = 1
N= int(input("Enter a number to e factorial: "))
for i in range(1, N+1):
    fact*=i
print(f'factorial of {N} is: {fact}')

# 7. Write a python script to count digits in a given number

num = int(input("Enter a Number: "))
print(f"{num} has {len(str(num))} digits")

# 8. Write a python script to calculate sum of digits of a given number
num = int(input("Enter a Number: "))
sum = 0
for i in str(num):
    sum += int(i)
print(f"sum of digits of number {num} is: {sum}")

# 9. Write a python script to print binary equivalent of a given decimal number. (do not use bin() method)

# using for loop
num = int(input("Enter a Number: "))
r=0
n = num
for i in range(n):
    r+=1
    if n // 2 == 0:
        break
    n = n // 2

binary = ''
for i in range(r):
    d = num //2
    r = num - d*2
    binary += str(r)
    num = d
print('0b'+binary[::-1])

# using while loop
num = int(input("Enter a Number: "))
binary = ''
while num > 0:

    d = num //2
    r = num - d*2
    binary += str(r)
    num = d
print('0b'+binary[::-1])


# 10. Write a python script to print the octal equivalent of a given decimal number. (do not use oct() method).

# using for loop
num = int(input("Enter a Number: "))
r=0
n = num
for i in range(n):
    r+=1
    if n // 8 == 0:
        break
    n = n // 8
print(r)
octal = ''
for i in range(r):
    d = num //8
    r = num - d*8
    octal += str(r)
    num = d
print('0o'+octal[::-1])

# using while loop
num = int(input("Enter a Number: "))
octal = ''
while num > 0:

    d = num //8
    r = num - d*8
    octal += str(r)
    num = d
print('0o'+octal[::-1])