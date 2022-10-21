# 1. Write a python script to print MySirG N times on the screen
n = 1
N = int(input("How many times you want to print MySirG on the screen? : "))
while n <= N:
    print("MySirG")
    n +=1

# 2. Write a python script to print first N natural numbers
n = 1
N = int(input("How many first natural numbers you want? : "))
print(f"First {N} Natural numbers are: ")
while n <= N:
    print(n,end=' ')
    n +=1

# 3. Write a python script to print first N natural numbers in reverse order

N = int(input("How many first natural numbers you want in reverse order? : "))
print(f"First {N} Natural numbers in reverse order are: ")
while N > 0:
    print(N,end=' ')
    N -=1

# 4. Write a python script to print first N odd natural numbers

num = 1
N = int(input(f"How many first odd natural numbers you want? : "))
print(f"First {N} Odd Natural numbers are: ")
while N >0:
    print(num, end=' ')
    num += 2
    N -= 1

# 5. Write a python script to print first N odd natural numbers in reverse order

N = int(input("How many first odd natural numbers you want in reverse order? : "))
print(f"First {N} Odd Natural numbers in reverse order are: ")
while N > 0:
    print(2*N-1,end=' ')
    N -=1

# 6. Write a python script to print first N even natural numbers
num = 2
N = int(input(f"How many first Even natural numbers you want? : "))
print(f"First {N} Even Natural numbers are: ")
while N >0:
    print(num, end=' ')
    num += 2
    N -= 1

# 7. Write a python script to print first N even natural numbers in reverse order
N = int(input("How many first Even natural numbers you want in reverse order? : "))
print(f"First {N} Even Natural numbers in reverse order are: ")
while N > 0:
    print(2*N,end=' ')
    N -=1

# 8. Write a python script to print squares of first N natural numbers

n = 1
N = int(input(f"How many squares of first N natural numbers you want? : "))
print(f"First {N} squares of natural numbers are: ")
while n <= N:
    print(n**2,end=' ')
    n += 1

# 9. Write a python script to print cubes of first N natural numbers

n = 1
N = int(input(f"How many Cubes of first N natural numbers you want? : "))
print(f"First {N} Cubes of natural numbers are: ")
while n <= N:
    print(n**3,end=' ')
    n += 1

# 10. Write a python script to print first 10 multiples of N
n = 1
N = int(input("Enter a number to find its first 10 multiples "))
while n <= 10:
    print(n*N, end=' ')
    n += 1

