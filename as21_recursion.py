# 1. Write a recursive python function to print first N natural numbers.

def printN(n) :
    if n > 0 :
        printN(n-1)
        print(n)
printN(5)

# 2. Write a recursive python function to print first N natural numbers in reverse order
def printNrev(n) :
    if n > 0 :
        print(n)
        printNrev(n-1)
printNrev(5)

# 3. Write a recursive python function to print first N odd natural numbers

def print_odd(n) :
    if n > 0:
        print_odd(n - 1)
        print(n + n - 1)
print_odd(5)

# 4. Write a recursive python function to print first N odd natural numbers in reverse order

def print_odd_rev(n) :
    if n > 0 :
        print(n + n - 1)
        print_odd_rev(n - 1)
print_odd_rev(6)

# 5. Write a recursive python function to print first N even natural numbers.

def print_even(n) :

    if n > 0 :
        print_even(n - 1)
        print(n*2)
print_even(6)

# 6. Write a recursive python function to print first N even natural numbers in reverse order.

def print_even_reverse(n) :

    if n > 0 :
        print(n * 2)
        print_even_reverse(n - 1)

print_even_reverse(7)

# 7. Write a recursive python function to print squares of first N natural numbers

def squareN(n) :
    if n == 1 :
        return 1
    return n*n + squareN(n-1)
s = squareN(5)
print(s)

# 8. Write a recursive python function to print cubes of first N natural numbers

def cubN(n) :
    if n == 1 :
        return 1
    return n**3 + cubN(n - 1)
c = cubN(5)
print(c)

# 9. Write a recursive python function to print first N multiples of a given number.

def Nmultiples(n, num) :
    if n > 0 :
        Nmultiples(n-1, num)
        print(num*n)
Nmultiples(5, 4)

# 10. Write a recursive python function to print a number in reverse order.

def reverse(n) :

    if len(str(n)) == 1:
        print(int(str(n)[0]))
    else:
        print(int(str(n)[-1]), end='')
        reverse(int(str(n)[:-1]))
reverse(123456789)