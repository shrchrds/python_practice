# 1. Write a recursive python function to calculate sum of first N natural numbers

def natural_sum(N):
    if N == 1:
        return 1
    return N + natural_sum(N-1)
ns = natural_sum(5)
print(f"sum of first N natural numbers: {ns}")

# 2. Write a recursive python function to calculate sum of first N odd natural numbers

def odd_sum(N):

    if N == 1:
        return 1
    return 2*N - 1 + odd_sum(N-1)
os = odd_sum(5)
print(f"Sum of first N odd natural numbers: {os}")

# 3. Write a recursive python function to calculate sum of first N even natural numbers

def even_sum(N):

    if N == 1:
        return 2
    return 2*N + even_sum(N-1)
es = even_sum(5)
print(f"Sum of first N even natural numbers: {es}")

# 4. Write a recursive python function to calculate sum of squares of first N natural numbers

def squareN(N):
    if N == 1:
        return 1
    return N*N + squareN(N-1)
squares = squareN(5)
print(f"Sum of squares of first N even natural numbers: {squares}")

# 5. Write a recursive python function to calculate sum of cubes of first N natural numbers

def cubeN(N):
    if N == 1:
        return 1
    return N**3 + cubeN(N-1)
cubes = cubeN(5)
print(f"sum of cubes of first N natural numbers: {cubes}")

# 6. Write a recursive python function to calculate the factorial of a number.

def factorial(N):
    if N == 1:
        return 1
    return N*factorial(N-1)
fact = factorial(5)
print(f"Factorial of 5 is: {fact}")

# 7. Write a recursive python function to calculate sum of the digits of a given number

def sum_digit(N):
    if len(str(N)) == 1:
        return N
    return sum_digit(int(str(N)[:-1])) + int(str(N)[-1])
sd = sum_digit(1555)
print(f"sum of digits of given number: {sd}")

# 8. Write a recursive python function to print binary of a given decimal number.

def decimal2binary(N):
    if N//2 >= 1:
        decimal2binary(N//2)
    print(N % 2, end='')
decimal2binary(10)


# 9. Write a recursive python function to print octal of a given decimal number

def decimal2octal(N):
    if N//8 >=1:
        decimal2octal(N//8)
    print(N % 8, end='')
decimal2octal(21)

# 10. Write a recursive python function to find the Nth term of the Fibonacci series

def fibonacci(N):
    if N == 0:
        return 0
    elif N <= 2:
        return 1
    else:
        return fibonacci(N-1) + fibonacci(N-2)
print(fibonacci(9))
