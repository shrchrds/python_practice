# 1. Write a python program to create a function that takes a list and returns a new list with the original list's unique elements.

def unique_list(lst) :
    return list(set(lst))
ul = unique_list([1,2,31,1,2,4,5,6,7,4,5,2,1,5,54,67,3,4,5])
print(ul)

# 2. Write a python program to create a function that takes a number as a parameter and checks if the number is prime or not.

def check_prime(n) :
    for i in range(2,n) :
        if n % i == 0 :
            return f"{n} is Not a Prime Number"
    return f"{n} is a Prime Number"
p = check_prime(11)
print(p)

# 3. Write a python program to create a function that prints the even numbers from a given list.
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def even_num(lst) :
    print(f"Even numbers from list are: ")
    for num in lst :
        if num % 2 == 0 :
            print(num, end=' ')
even_num(lst)

# 4. Write a python program to create a function that checks whether a passed string is palindrome or not.

def check_palindrome(string) :
    if string == string[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")
check_palindrome("kayak")

# 5. Write a python program to create a function to find the Min of three numbers.

def check_min(num1,num2,num3) :
    return f"Minimum Number from {num1}, {num2} and {num3}, is: {min((num1, num2, num3))}"
print(check_min(3,5,2))

def check_min(num1,num2,num3) :
    if num1 < num2 and num1 < num3 :
        print(f"{num1} is minimum number from {num1}, {num2} and {num3}")
    elif num2 < num1 and num2 < num3 :
        print(f"{num2} is minimum number from {num1}, {num2} and {num3}")
    else:
        print(f"{num3} is minimum number from {num1}, {num2} and {num3}")
check_min(3,5,2)

# 6. Write a python program to create a function and print a list where the values are square of numbers between 1 and 30.

def square_list(num1, num2) :
    squares = [i**2 for i in range(num1,num2+1)]
    print(f"Square of numbers between {num1} and {num2} \n {squares}")
square_list(1,30)

# 7. Write a python program to access a function inside a function.

def numerical_operations(num1, num2):
    def add(num1,num2) :
        return f"Addition of {num1} and {num2} is: {num1 + num2}"

    def substract(num1, num2) :
        return f"Substraction of {num1} and {num2} is: {num1 - num2}"

    return f"{add(num1, num2)} \n{substract(num1, num2)}"
# numerical_operations(2,4)
num_ops = numerical_operations(2,4)
print(num_ops)

# 8. Write a python program to create a function that accepts a string and calculate the number of upper case letters and lower case letters.

def upper_lower(string):
    upper = lower = 0
    for chr in string:
        if chr.isupper():
            upper +=1
        elif chr.islower():
            lower +=1
    return f"No of upper case letters are: {upper}\nNo of lower case letters are: {lower}"
print(upper_lower('I am Indian'))

# 9. Write a python program to create a function to check whether a string is a pangram or not.

def panrgam_check(string):
    pangram = True
    for i in 'abcdefghijklmnopqrstuvwxyz':
        if i in set(string.lower()):
            pass
        else:
            pangram = False
    if pangram == False:
            print("Given string is not panagram")
    else:
        print("Given string is panagram")
panrgam_check("Cwm fjord veg balks nth pyx quiz")
panrgam_check("A quick brown fox jumps over the lazy dog")
panrgam_check("Quick zephyrs blow, vexing daft Ji")

# 10. Write a python program to create a function to check whether a string is an anagram or not.

def anagram_check(string1, string2):
    if set(string1) == set(string2):
        print(f"{string1} and {string2} are anagrams")
    else:
        print(f"{string1} and {string2} are not anagrams")
anagram_check('race','care')
anagram_check('india', 'daniel')
