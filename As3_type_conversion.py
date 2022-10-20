# 1. Write a python script to convert a number into str type.

num = int(input("Enter a number: "))
print(str(num))

# 2. Write a python script to print Unicode of the character ‘m’
print(ord('m'))

# 3. Write a python script to print character representation of a given unicode 100.
print(chr(100))

# 4. Write a python script to print any number and its binary equivalent
num = int(input("Enter a number: "))
print(f'Binary equivalent of {num} is: {bin(num)}')

# 5. Write a python script to print any number and its octal equivalent.
num = int(input("Enter a number: "))
print(f'Octal equivalent of {num} is: {oct(num)}')

# 6. Write a python script to print any number and its hexadecimal equivalent.
num = int(input("Enter a number: "))
print(f'hexadecimal equivalent of {num} is: {hex(num)}')

# 7. Write a python script to store binary number 1100101 in a variable and print it in decimal format.
bin_num = 1100101
print(f"Decimal of {bin_num} is: {int(str(bin_num),2)}")

# 8. Write a python script to store a hexadecimal number 2F in a variable and print it in octal format.
hex_num = "2F"
dec_num = int(hex_num,16)
print(f"Hexadecimal of {hex_num} is: {oct(dec_num)}")

# 9. Write a python script to store an octal number 125 in a variable and print it in binary format.
oct_num  = 125
dec_num = int(str(oct_num), 8)
print(f"Binary equivalent of {oct_num} is: {bin(dec_num)}")

# 10. Write a python script to add two numbers 25 (in octal) and 39 (in hexadecimal) and display the result in binary format.
oct_num1 = 25
hex_num2 = 39
dec_num1 = int(str(oct_num1),8)
dec_num2 = int(str(hex_num2),16)
print(f"Binary equivalent of octal number{oct_num} and hexadecimal number {hex_num2} is: {bin(dec_num1 + dec_num2)}")
