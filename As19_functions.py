# 1. Write a python program to create a simple function which prints “MySirG” .

def mysirg():
    print("MySirG")
mysirg()

# 2. Write a python program to create a function which expects two arguments and print them in the function body.

def twoargs(a,b):
    print(a)
    print(b)
twoargs(4,5)

# 3. Write a python program to create a function which expects an unknown number of arguments.

def unkwown_args(*args):
    print(args)
unkwown_args(1,2,3,4,5)

# 4. Write a python program to create a function which expects kwargs arguments

def kwargs_funct(a=2,b=3):
    print(a)
    print(b)
kwargs_funct(3,4)

# 5. Write a python program to create a function which expects a list as an argument.

def list_funct(list1:list):
    print(list1)
list_funct([5,6])

# 6. Write a python program to create a function that finds a maximum of four numbers.

def maxof4(a,b,c,d) :
    if a > b and a > c and a > d :
        print(f"Maximum of {a},{b},{c},{d} numbers is: {a}")
    elif b > a and b > c and b > d :
        print(f"Maximum of {a},{b},{c},{d} numbers is: {b}")
    elif c > a and c > b and c > d :
        print(f"Maximum of {a},{b},{c},{d} numbers is: {c}")
    else:
        print(f"Maximum of {a},{b},{c},{d} numbers is: {d}")
maxof4(1,2,3,4)

# 7. Write a python program to sum all the numbers in a list.

def sum_list(lst:list) :
    summ = 0
    for i in lst :
        summ += i
    print(f"Sum of all the members in {lst} list is: {summ}")
sum_list([1,2,3,4])

# 8. Write a python program to multiply all the numbers in a list.

def multiply_list(lst:list) :
    mul = 1
    for i in lst:
        mul = mul * i
    return f"Multiplication of all the elements in {list} is: {mul}"
print(multiply_list([11,2,3,4]))

# 9. Write a python program to create a function to check whether a number falls in a given range.

def check_range_number(num, lower, upper) :
    if num >= lower and num <= upper :
        print(f"{num} is in range of {lower} and {upper}")
check_range_number(5, 1, 10)

# 10. Write a python program to create a function to check whether a given number is even or odd.

def even_odd(num) :
    if num % 2 == 0 :
        print(f"{num} is even number")
    elif num % 2 == 1:
        print(f"{num} is odd number")
even_odd(5)