# 1. Write a Python script to create a list of first N natural numbers

N= int(input("Enter a number to create a list of first N natural numbers: "))
first_N_num = [i for i in range(1,N+1)]
print(f"list of first{N} natural numbers: {first_N_num}")

# 2. Write a Python script to create a list of first N odd natural numbers.

N= int(input("Enter a number to create a list of first N odd natural numbers: "))
first_N_odd = [(2*i - 1) for i in range(1,N+1)]
print(f"list of first {N} odd natural numbers: {first_N_odd}")

# 3. Write a Python script to create a list of first N even natural numbers

N= int(input("Enter a number to create a list of first N odd natural numbers: "))
first_N_even = [2*i for i in range(1,N+1)]
print(f"list of first {N} even natural numbers: {first_N_even}")

# 4. Write a Python script to find the greatest number in a given list of numbers

lst = eval(input("Enter a list: "))
max_num = lst[0]
for i, num in enumerate(lst):
    if num > max_num:
        max_num = num
print(f"Maximum Number from list: {max_num}")

# 5. Write a Python script to find the smallest number in a given list of numbers.

lst = eval(input("Enter a list: "))
smallest_num = lst[0]
for i, num in enumerate(lst):
    if num < smallest_num:
        smallest_num = num
print(f"Smallest Number from list: {smallest_num}")

# 6. Write a Python script to calculate the sum of elements in a given list of numbers.
sum = 0
lst = eval(input("Enter a list: "))
for i in lst:
    sum += i
print(f"the sum of elements in a given list of numbers: {sum}")

# 7. Write a Python script to remove all non int values from a list.

lst = eval(input("Enter a list: "))
for i, ele in enumerate(lst):
    if type(ele) != int:
        lst.pop(i)
print(f"Final list after removing non int values: {lst}")

# 8. Write a Python script to print distinct elements along with their frequencies of occurrence in the list.

lst = eval(input("Enter a list: "))
distinct_elements = set(lst)
for i, ele in enumerate(distinct_elements):
    print(f"Count of element {ele}: {lst.count(ele)}")

# 9. Write a Python script to print indices of all occurrences of a given element in a given list.

lst = eval(input("Enter a list: "))
ele = eval(input("Enter an element to find its all occurrences if a list: "))

for i, e in enumerate(lst):
    if e == ele:
        print(i)

# 10. Write a python script to sort a list.

lst = eval(input("Enter a list: "))
print(f"Sorted list in ascending order: {sorted(lst)}")