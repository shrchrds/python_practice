# 1. Write a python script to add comments and print “Learning Python” on screen.

# python basic program
print("Learning Python")

# 2. Write a python script to add multi line comments and print values of four variables, each in a new line. Variable contains any values.

"""adding multi line comment
printing values of four variables each in a new line    
"""
language = input("Enter programming language: ")
version = float(input("Enter a version of language: "))
app = input("Enter which app you are developing: ")
use = input("Enter use of app: ")
print(language)
print(version)
print(app)
print(use)

# 3. Write a python script to print types of variables. Create 5 variables each of them containing different types of data. (like 35, True, “MySirG”,5.46, 3+4j, etc)

language = 'Python'
python_version = 3.9
revision = 3
update = False
complex = 5 + 4j
print(type(language))
print(type(python_version))
print(type(revision))
print(type(update))
print(type(complex))

# 4. Write a python script to print the id of two variables containing the same integer values.

a = 5
b = 5
print(id(a))
print(id(b))

# 5. Create four variables in a Python script and assign values of different data types to them. Write a Python script to print value, its type and id of each variable
language = 'Python'
python_version = 3.9
revision = 3
update = False

print(f"Language: {language}, Data type: {type(language)}, ID: {id(language)}")
print(f"Python Version: {python_version}, Data type: {type(python_version)}, ID: {id(python_version)}")
print(f"Revision: {revision}, Data type: {type(revision)}, ID: {id(revision)}")
print(f"Update: {update}, Data type: {type(update)}, ID: {id(update)}")

# 6. Write a python script to print all the keywords
import keyword
print(f"Keyword list in python: {keyword.kwlist}")

# 7. On Python shell use help() function and display the list of keywords
# go to shell > type following
import keyword
print(f"Keyword list in python: {keyword.kwlist}")

# 8. Create two Python files A0.py and A1.py. Create a variable in A1.py and assign some value to it.
# Write a python script to import A1 module in A0 and print value of the variable created in A0.py

# create A0.py file and A1.py file
# go to A1.py file, create variable name = "Hare Krishna"
# go to A0.py file and type following
import A1
print(A1.name)

# 9. Name the keywords, used as data in the Python script.
print(list)
print(type(str))
print(False)

# 10. Write a python script to display the current date and time. First create variables to store date and time, then display date and time in proper format (like: 13-8-2022 and 9:00 PM)
import datetime
date = datetime.datetime.today()
print(f"Todays date is: {date.day}-{date.month}-{date.year} and current time is: {date.hour}:{date.minute} ")