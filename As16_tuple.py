# 1. Write a python script to store multiple items in a single variable ( Items are “Java” ,“Python”, “SQL”, “C” ) using tuple
t1 = ("Java", "Python", "SQL", "C")
print(t1, type(t1))

# 2. Write a python program to store only one item using tuple
t2 = (2,)
print(t2, type(t2))

# 3. Write a python program to reverse the tuple
tup = eval(input("Enter a tuple to reverse: "))
rev_tup = list(tup)[::-1]
print(f"Reversed tuple: {tuple(rev_tup)}")

# 4. Write a python program to Swap two tuples in Python.
tup1 = eval(input("Enter a tuple1: "))
tup2 = eval(input("Enter a tuple2: "))
tup1, tup2 = tup2, tup1
print(tup1)
print(tup2)

# 5. Write a python program to check if all items in the tuple are the same

tup = eval(input("Enter a tuple: "))
count = 0
for item in tup:
    if item == tup[0]:
        count +=1
if count == len(tup):
    print("All items in the tuple are the same")
else:
    print("All items in the tuple are not the same")

# 6. Write a python program to divide the tuple into four variables. tuple1=(100, 200, 300, 400)
tuple1=(100, 200, 300, 400)
v1, v2,v3,v4 = tuple1[0], tuple1[1], tuple1[2], tuple1[3]
print(v1)
print(v2)
print(v3)
print(v4)

# 7. Write a python program to copy elements 4 and 5 from the following tuple into a new tuple. tuple1=(1,2,3,4,5,6)
tuple1 = (1,2,3,4,5,6)
tuple2 = tuple1[3:5]
print(tuple2)

# 8. Write a python program to Sort a tuple of tuples by the second item.
tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))
tup = sorted(tuple1, key= lambda x:x[1])
print(tup)


# 9. Write a python program to print the value 20 from given nested tuple
tuple1 = ("Python", [10, 20, 30], (2, 4, 16))
print(tuple1[1][1])

# 10. Write a python program to change the first item (22) of a list within the following tuple to 222.
tuple1 = (11, [22, 33], 44, 55)
tup2 = list(tuple1)
tup2[1][0] = 222
print(tup2)
tuple1 = tuple(tup2)
print(tuple1)