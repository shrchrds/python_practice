# 1. Write a python script to print the first 10 multiples of 5.

for i in range(10):
    print(5*(i+1), end=' ')

# 2. Write a python script to print first 10 multiples of N
N= int(input("Enter a number to print first 10 multiples: "))
for i in range(10):
    print(N*(i+1), end=' ')

# 3. Write a python script to print first M multiples of N.
M = int(input("How many multiples you want?: "))
N= int(input(f"Enter a number to print first {M} multiples: "))

for i in range(M):
    print(N*(i+1), end=' ')

# 4. Write a python script to print the first 10 multiples of N in reverse order

N= int(input("Enter a number to print first 10 multiples: "))
for i in range(10,0,-1):
    print(N*i, end=' ')

# 5. Write a python script to print table of user’s choice
N= int(input("Enter a number to print its table: "))
print(f"{N}'s table is: ")
for i in range(10):
    print(f"{N}*{i+1} = {N*(i + 1)}")

# 6. Write a python script to print first N even natural numbers.

N= int(input("Enter a number to print first even natural numbers: "))
for i in range(N):
    print(2*(i+1), end=' ')

# 7. Write a python script to print first N odd natural numbers

N= int(input("Enter a number to print first odd natural numbers: "))
for i in range(N):
    print(2*(i+1)-1, end=' ')

# 8. Write a python script to print squares of first N natural numbers.

N= int(input("Enter a number to print squares of first N natural numbers: "))
for i in range(N):
    print((i+1)**2, end=' ')

# 9. Write a python script to print cubes of first N natural numbers.

N= int(input("Enter a number to print cubes of first N natural numbers: "))
for i in range(1,N+1):
    print(i**3, end=' ')

# 10. Write a python script to display all prime numbers within a range, start = 15, end = 45
print("Prime numbers in  a range of 15 to 45 are: ")
for num in range(15, 46):

    for i in range(2,num):
        if num % i == 0:
            break
    else:
        print(num)
