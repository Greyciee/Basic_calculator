# Basic Calculator Program

# Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
# Perform the operation based on the user's input and print the result.
# Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.

first_num = int(input("Enter a number "))
second_num = int(input("Enter another number "))
print("Great!")
maths_sign = input("now enter a mathematical operation (+, -, *, or / )  ")
print("Result Processing...")

if maths_sign == "+":
    result = first_num + second_num
    print(f"{first_num} {maths_sign} {second_num} = {result} " )
elif maths_sign == "-" :
    result = first_num - second_num
    print(f"{first_num} {maths_sign} {second_num} = {result} " )
elif maths_sign == "*" :
    result = first_num * second_num
    print(f"{first_num} {maths_sign} {second_num} = {result} " )
elif maths_sign == "/" :
    if second_num != 0:
        result = first_num / second_num
        print(f"{first_num} {maths_sign} {second_num} = {result} " )
    
    else:
        print("Error: Division by Zero is not allowed.")
else:
    print("Error:Incorrect mathematical operation. Please use +, -, *, or /.")
    

