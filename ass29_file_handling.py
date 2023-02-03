# 1. Write a Python script to print the following status of a file:
#     a. Whether a file is read only
#     b. Whether a file is closed or not
#     c. Which file opening mode is used
#     d. Name of the file

with open("fh.txt" ,"w") as f:
    f.write("This is sample file")

with open("fh.txt" ,"w") as f:
    print("Read only" if f.mode == "r" else "Write file")
    print(f.closed)
    print(f.mode)
    print(f.name)

# 2. Write a Python script to create a new file ‘myfile.txt’ and store user entered text.
with open("myfile.txt", "w") as f:
    f.write(input("Enter a content to write: "))

# 3. Write a Python script to read the above created file ‘myfile.txt’ and display content on the console.
with open("myfile.txt", "r") as f:
    content = f.read()
    print(content)

# 4. Write a Python script to store a list of city names in a file ‘cities.txt’
with open('cities.txt', 'w') as f:
    f.write("Pune, Mumbai, Bhopal, Bangalore, Delhi, Chennai, Kolkata")
with open("cities.txt", "r+") as f:
    data = f.readlines()
    f.write(str(data))
    print(data)

# 5. Write a Python script to append list of city names in a file ‘cities.txt’
with open("cities.txt", "a") as f:
    f.write("\n")
    f.write(str(['Noida', "Baroda", "Mysore"]))
with open("cities.txt", "r") as f:
    data = f.read() 
    print(data)

# 6. Write a Python script to search whether a particular city is there in the file ‘cities.txt’ or not

def search(filename, word):
    with open(filename, "r") as f:
        data = f.read()
    if word in data:
        print(f"{word} is present in {filename}")
    else:
        print(f"{word} is not present in {filename}")

search('cities.txt', 'Pune')

# 7. Write a Python script to count the number of Python keywords occurring in a python source file.
from keyword import kwlist
print(f"No of keywords present in Python Source file are:  {len(kwlist)}")

# 8. Write a Python script to create a copy of a file.
with open("cities.txt", "r") as f:
    data = f.read()
with open("new_city", "w") as f:
    f.write(data)

# 9. Write a Python script to store book data in a file. Book data is in the form of a
# dictionary in which book name is the key and price is its value. Use pickle to store
# data into a file (say bookfile)

book_data = {"Rich Dad Poor Dad": 300}
import pickle
with open("bookfile", "ab") as f:
    pickle.dump(book_data, f)

# 10. Write a Python script to extract book data from a bookfile using pickle. Also print extracted book data.
import pickle
with open("bookfile", "rb") as f:
    s = pickle.load(f)
    [print(key, s[key]) for key in s]