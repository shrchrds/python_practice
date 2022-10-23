# 1. Write a python script to store multiple items in a single variable ( Items are “Java” ,“Python”, “SQL”, “C” ) using list

lst = []
while True:
    item = input("Enter an item to add in a list: ")
    lst.append(item)
    new_item = input("Do you want to add a new item in list?[y/n]: ")
    if new_item == 'n':
        break
print(f"Final List of items: {lst}")

# 2. Write a python script to get the data type of a list.
lst = eval(input("Enter a list: "))
[type(i) for i in lst]

# 3. Write a python script to get the last item of the list ( mylist = ["Java", "C", "Python"])
lst = eval(input("Enter a list: "))
print(f"Last item of the list: {lst[-1]}")

# 4. Write a python script to Change the values "SQL" and "Reactnative" with the values "NoSQL" and "Flutter" 
# (List is thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]

thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
for i, item in enumerate(thislist):
    if item == "SQL":
        thislist[i] = "NoSQL"
    elif item == "Reactnative":
        thislist[i] = "Flutter"
print(thislist)

# 5. Write a python script to add an item to the end of the list (item “Python”. (mylist = ["Java", "SQL", "C", "Reactnative"]
mylist = ["Java", "SQL", "C", "Reactnative"]
mylist.append("Python")
print(mylist)

# 6. Write a python program to append elements from another list to the current list.
# (firstlist = ["Java", "Python", "SQL"], secondlist = ["C", "Cpp", "NoSQL"] )

firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"]
firstlist.extend(secondlist)
print(firstlist)

# 7. Write a python program to Print all items by referring to their index number 
# (thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]

thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
for i in thislist:
    print(i)

# 8. Write a python program to sort the list alphanumerically – thislist = ["Java", "SQL", "C", "Reactjs", "Javascript", "Python"]

thislist = ["Java", "SQL", "C", "Reactjs", "Javascript", "Python"]
thislist.sort()
print(thislist)

# 9. Write a Python script to create a list of city names taken from the user.

city_lst = []
while True:
    city = input("Enter city name to add in a list: ")
    city_lst.append(city)
    new_city = input("Do you want to add a new item in list?[y/n]: ")
    if new_city == 'n':
        break
print(f"Final List of cities: {city_lst}")

# 10. Write a Python script to create a list, where each element of the list is a digit of a given number.

number = input("Enter a number: ")
[int(i) for i in str(number) ]
