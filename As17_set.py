# 1. Write a python program to store all the programming languages known to you using Set.

languages = {"Python", "C", "C++", "Java", "Scala","JavaScript", "SQL"}
print(f"Programming languages: {languages}")

# 2. Write a python program to store your own information {name, age, gender, so on..}

info = {'Ashok', 32, "Male", "Assistant Professor", "1 Child"}
print(info)

# 3. Write a python script to get the data type of a Set.
set_ = {"Python", "C", "C++", "Java", "Scala"}
print(type(set_))

# 4. Write a Python script to find if “Python” is present in the set thisset = {"Java", "Python", "Django"}
thisset = {"Java", "Python", "Django"}
if "Python" in thisset:
    print(f'Python is present in {thisset}')
else:
    print(f'Python is NOT present in {thisset}')

# 5. Write a python program to add items from another set to the current set. thisset = {"Java", "Python", "SQL"}, secondset= {"C", "Cpp", "NoSQL"}

thisset = {"Java", "Python", "SQL"}
secondset= {"C", "Cpp", "NoSQL"}
for ele in secondset:
    thisset.add(ele)
print(thisset)

# 6. Write a python program to add elements of list to a set. thisset = {"Python", "Django", "JavaScript"}, mylist = ["Java", "C"]

thisset = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]
for ele in mylist:
    thisset.add(ele)
print(thisset)

# 7. Write a python program to remove last item of the given set.
thisset = {"Python", "Django", "JavaScript", "SQL"}
thisset.discard("SQL")
print(thisset)

thisset = {"Python", "Django", "JavaScript", "SQL"}
thisset.remove("SQL")
print(thisset)

# 8. Write a python program to delete the set completely.
thisset = {"Python", "Django", "JavaScript", "SQL"}
del thisset

# 9. Write a python program to loop through the set and print values
thisset = {"Python", "Django", "JavaScript", "SQL"}
for ele in thisset:
    print(ele)

# 10. Write a python program to find the maximum and minimum value in a set.
numbers = {12,34,10,7, 66}
print(f"Maximum number in a set: {max(numbers)}")
print(f"Minimum number in a set: {min(numbers)}")
