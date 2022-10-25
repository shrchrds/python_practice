# 1. Write a python program to create and print a dictionary which stores your information. (name, age, gender …..)
info = {"Name": "Ashok", "Age": 30, "Gender": "Male", "Profession":"Assistant Professor", "Salary": 63000}
print(info)

# 2. Write a python program to access the items of a dictionary by referring to its key name.
info = {"Name": "Ashok", "Age": 30, "Gender": "Male", "Profession":"Assistant Professor", "Salary": 63000}
print(f"Name of person is: {info['Name']}")

# 3. Write a python program to get a list of the values from a dictionary.
info = {"Name": "Ashok", "Age": 30, "Gender": "Male", "Profession":"Assistant Professor", "Salary": 63000}
print(f"Values present in dictionary: {info.values()}")

# 4. Write a python program to change the value of a specific item by referring to its key name.
info = {"Name": "Ashok", "Age": 30, "Gender": "Male", "Profession":"Assistant Professor", "Salary": 63000}
info['Salary'] = 75000
print(f"Updated Salary for Ashok: {info['Salary']}")

# 5. Write a python program to print all key names in the dictionary, one by one.
for key in info.keys():
    print(key)

# 6. Write a python program to create a dictionary that contains three dictionaries. (nested)
info = {"Name": "Ashok", "Age": 30, "Gender": "Male", "Profession":"Assistant Professor", "Salary": 63000}
info.update({"KYC":{"PAN":"BVFA87654P", "Adhar": 234567789}})
info.update({"Property":{"Land": "2 Acre", "Flat":"2BHK", "Car": "Hyundai Grand i10 Nios" }})
print(info)

# 7. Write a python program to create three dictionaries, then create one dictionary that will contain the other three dictionaries.
ashok  = {"Name": "Ashok", "Age": 30, "Gender": "Male", "Profession":"Assistant Professor", "Salary": 63000}
harsh = {"Name": "Harshavardhan", "Age": 35, "Gender": "Male", "Profession":"Associate Professor", "Salary": 71000}
mak = {"Name": "Makrand", "Age": 43, "Gender": "Male", "Profession":"Professor", "Salary": 111000}
employees = {"Teaching":{"Ashok":ashok, "Harshavardhan":harsh, "Makarand":mak}}
print(employees)

# 8. Write a python program to convert two lists into a dictionary in a way that item from list1 is the key and item from list2 is the value.
names = ["Ashok", "Harshavardhan", "Makarand"]
ages = [30,35, 43]
data = dict(zip(names,ages))
print(data)

# 9. Write a python program to merge two python dictionaries into one dictionary.
ashok = {"Name": "Ashok", "Age": 30, "Gender": "Male", "Profession":"Assistant Professor", "Salary": 63000}
kyc = {"KYC":{"PAN":"BVFA87654P", "Adhar": 234567789}}
ashok.update(kyc)
print(ashok)

# 10. Write a python program to get the key of lowest value from the dictionary.
sample_dict = {'C': 92,'Java': 66,'Python': 85}
min_value = min(sample_dict.values())
for key,value in sample_dict.items():
    if value == min_value:
        print(f"Key of Minimum value: {key}")
