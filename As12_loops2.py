# 1. Write a python script to reverse a number.

num = int(input("Enter a Number: "))
print(f"Reversed number: {int(str(num)[::-1])}")

# 2. Write a python script to check whether a given number is Prime or not

num = int(input("Enter a Number: "))
for i in range(2, num):
    if num % i == 0:
        print(f"{num} is Not a Prime Number")
        break
    else:
        print(f"{num} is a Prime Number")
        break

# 3. Write a python script to print all Prime numbers under 100

for num in range(1,100):
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        print(num, end=' ')
# 4. Write a python script to print all Prime numbers between two given numbers (both values inclusive)

num1 = int(input("Enter a Number1: "))
num2 = int(input("Enter a Number2: "))

for num in range(num1, num2+1):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=' ')

# 5. Write a python script to find next prime number of a given number

num = int(input("Enter a Number: "))
for num in range(num, num*2):
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        print(f"Next Prime number is: {num}")
        break

# 6. Write a python script to print first N prime numbers
N= int(input("Enter a number to print first N prime numbers: "))
prime_numbers = []
for num in range(1, N*3):
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        prime_numbers.append(num)
        if len(prime_numbers) == N:
            break
print(f"First {N} Prime numbers are: {prime_numbers}", end=' ')

# 7. Write a python script to check whether a given pair of numbers are co-Prime numbers or not

num1 = int(input("Enter a Number1: "))
num2 = int(input("Enter a Number2: "))
cf1 = set()
cf2 = set()
for i in range(1,num1+1):
    if num1 % i == 0:
        cf1.add(i)
for j in range(1,num2+1):
    if num2 % j == 0:
        cf2.add(j)
if cf1.intersection(cf2) == {1}:
    print(f"{num1} and {num2} are Co-Prime Numbers")
else:
    print(f"{num1} and {num2} are NOT Co-Prime Numbers")

# 8. Write a python script to print first N terms of a Fibonacci series

N= int(input("Enter a number to print first N terms of a Fibonacci series: "))
a,b = 0,1
for i in range(N):
    print(a, end=' ')
    a,b = b, a+b

# 9. Write a python script to calculate LCM of two numbers

n1 = int(input("Enter a Number1: "))
n2 = int(input("Enter a Number2: "))
n1_mul = {n1*i for i in range(1,max(n1,n2)+1)}
n2_mul = {n2*i for i in range(1,max(n1,n2)+1)}
print(f"LCM of {n1} and {n2} is: {min(n1_mul.intersection(n2_mul))}")

# 10. Write a python script to calculate HCF of two numbers

n1 = int(input("Enter a Number1: "))
n2 = int(input("Enter a Number2: "))
n1_fact = {i for i in range(2,n1+1) if n1%i==0}
n2_fact = {i for i in range(2,n2+1) if n2%i==0}
print(f"HCF of {n1} and {n2} is: {max(n1_fact.intersection(n2_fact))}")