# 1. Use iter and next method to access all the elements of a given set using while loop

s1 = {1, 2, 3, 4, 5}
it = iter(s1)
while True:
    try:
        print(next(it), end=' ')
    except:
        break


# 2. Create a generator to produce first n odd natural numbers

def generate_odd(n):
    x = 1
    while n:
        yield x
        x += 2
        n -= 1


for ele in generate_odd(5):
    print(ele)


# 3. Create a generator to produce first n even natural numbers

def generate_even(n):
    x = 2
    while n:
        yield x
        x += 2
        n -= 1


for ele in generate_even(5):
    print(ele)


# 4. Create a generator to produce squares of first N natural numbers

def generate_squares(n):
    x = 1
    while n:
        yield x ** 2
        x += 1
        n -= 1


for ele in generate_squares(5):
    print(ele)


def generate_squares(n):
    for i in range(1, n + 1):
        yield i ** 2


for ele in generate_squares(6):
    print(ele)


# 5. Create a generator to produce first n terms of Fibonacci series

def fib_series(n):
    a, b = 0, 1
    while n:
        yield a
        a, b = b, a + b
        n -= 1


for ele in fib_series(9):
    print(ele)


# 6. Create a generator to produce first n prime numbers

def produce_prime(N):
    prime_nums = []

    for n in range(1, 999):

        for i in range(2, n):

            if n % i == 0:
                break
        else:
            prime_nums.append(n)
    yield prime_nums[:N]


for ele in produce_prime(5):
    print(ele)


# 7. Create an endless iterator using generator method to produce terms of Fibonacci series

def fib_endless():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


it = fib_endless()
fib_num = []
while True:
    print("Do you want to generate another number?[y/n] : ")
    ans = input()

    if ans == 'y':
        x = next(it)
        print(x)
        fib_num.append(x)
    else:
        break
print(fib_num)


# 8. Create an endless iterator using generator method to produce Prime numbers


def produce_prime(N):
    prime_nums = []
    upp = 10
    for n in range(1, upp):

        for i in range(2, n):

            if n % i == 0:
                break
        else:
            prime_nums.append(n)
    yield prime_nums[:N]


for ele in produce_prime(5):
    print(ele)


# 9. Define a function which takes lengths of three sides of a triangle as arguments and display the perimeter of triangle.
# Define and apply a decorator which checks for the validity of the triangle on the basis of lengths of the side.
# This makes the perimeter to be displayed when the triangle can exist with the given lengths of the sides.

def decor_triangle(triangle_func):
    def valid_triangle(l1, l2, l3):
        if l1 < (l2 + l3) or l2 < (l1 + l3) or l3 < (l1 + l2):
            print("Triangle is valid")
        triangle_func(l1, l2, l3)

    return valid_triangle


@decor_triangle
def perimeter(l1, l2, l3):
    print(f"Perimeter of Triangle is: {l1 + l2 + l3}")


perimeter(10, 20, 50)

# 10. Define a function which calculates HCF of two numbers. Define and apply a decorator to check whether two given numbers are co-prime or not.

def decor_func(func):
    def co_prime(n1,n2):
        n1_fact = {i for i in range(1, n1) if n1 % i == 0}
        n2_fact = {i for i in range(1, n2) if n2 % i == 0}
        common = n1_fact.intersection(n2_fact)
        if common == {1}:
            print(f"{n1} and {n2} are Co prime numbers")
        func(n1,n2)
    return co_prime

@decor_func
def check_hcf(n1,n2):
    n1_fact = {i for i in range(1, n1) if n1 % i == 0}
    n2_fact = {i for i in range(1, n2) if n2 % i == 0}
    hcf = max(n1_fact.intersection(n2_fact))
    print(f"HCF of {n1} and {n2} is: {hcf}")

check_hcf(24,20)