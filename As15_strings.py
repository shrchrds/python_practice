# 1. Write a python script to create a String in 3 different possible ways

string1 = 'Python'
string2 = input("Enter your name: ")
str1 = 5
string3 = str(5)

print(string1)
print(string2)
print(string3)

# 2. Write a python script to Get the characters from the start to position 5 (Given String “iNeuron” using the slice syntax)

string = "iNeuron"
print(string[:5])

# 3. Write a python script to Get the characters from position 2 to position 5 (Given String “Hello Learners” using the slice syntax)

string = "Hello Learners"
print(string[1:5])

# 4. Write a python script to demonstrate String Concatenation adding space in between (Given Strings a=”Learning” b=”Python” )
a = "Learning"
b = "Python"
print(' '.join([a,b]))

# 5. Write a python script to get the count of total number of characters in String a= “iNeuron”

a = "iNeuron"
print(f"total number of characters in String a= “iNeuron”: {len(a)}")

# 6. Write a python script to reverse a String. (“iNeuron”)
a = "iNeuron"
print(f"reversed String: {a[::-1]}")

# 7. Write a python script to determine whether a string contains a specific substring

string = input("Enter a string: ")
substring = input("Enter substring to determine whether a string contains it: ")
if substring in string:
    print(f"{substring} is present in {string}")
else:
    print(f"{substring} is NOT present in {string}")

# 8. Write a python script to check if a string contains only numbers.
string = input("Enter a string: ")
if string.isnumeric():
    print(f"{string} contains only numbers")
else:
    print(f"{string} donot contains only numbers")

# 9. Write a python script to check if a string contains only characters of the alphabet

string = input("Enter a string: ")
if string.isalpha():
    print(f"{string} contains only characters of the alphabet")
else:
    print(f"{string} donot contains only characters of the alphabet")

# 10. Write a python script to convert an integer to a string

number = int(input("Enter a number: "))
print(f"integer to string: {str(number)}, type: {type(str(number))}")
