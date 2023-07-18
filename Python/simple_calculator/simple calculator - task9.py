# I will create a calculator allowing the user to perform simple mathematical equations. 

import math
import os

# I added a title and some characters to aid visualisation
char = "******"
print(f"{char}Welcome to your maths calculator{char}")

# A while loop with try and except to account for unexpected events and user inputs
while True:
    try:
   
        first_num = float(input("Input your first number: "))

        # Below I created a block to account for incorrect operator input, and to loop from the begining.
        math_operator = (input("Insert the symbol (+, -, *, /) of the operation you would like to perform: "))
        if math_operator == "+" or math_operator == "-" or math_operator == "*" or math_operator == "/":
            pass
        else:
            print("Invalid operator, please try again.") 
            continue
        
        second_num = float(input("Input your second number:"))

        # I created the calculation block by using the above created def and printed the equation and teh result.    
        if math_operator == "+":
            result = (first_num + second_num)
        elif math_operator == "-":
            result = (first_num - second_num)
        elif math_operator == "*":
            result = (first_num * second_num)
        elif math_operator == "/":
            result = (first_num / second_num)
    except ZeroDivisionError:
        print("Division by zero is undefined and does not result in a meaningful value, Try again." )   

    try: 
        print(f"Your input result is: {first_num} {math_operator} {second_num} = {result}")

        # The below block creates, reads and displays the file contents by asking the user to chose and also I accounted for some user errors 
        with open("User_inputs.txt", 'a') as file:
            file.write(f"{first_num} {math_operator} {second_num} = {result}\n")
    
        read_file = str(input("To see all the input calculations type 'User_inputs.txt' otherwise press enter: "))

        try:        
            with open(read_file, "r") as file:
                equations = file.read()
                print("Your equations entered are:")
                print(equations)
                        
        except FileNotFoundError:
            print("Invalid input, please try again.")

    except:
        print("Invalid input, please try again.")


        
# Reference:
# https://www.digitalocean.com/community/tutorials/how-to-make-a-calculator-program-in-python-3
# https://www.programiz.com/python-programming/user-defined-function
# HyperionDev lectures

