'''
In this make task, we will code our own simple calculator. 
You program should have 4 functions that add, subtract, multiply or divide two integer number arguments. 
The user is asked to input two numbers. These numbers will be passed as arguments into one of the subroutines. 
The user is asked to input 1 to add, 2 to subtract, 3 to multiply and 4 to divide. Output the returned result as part of a sentence.
'''

def add(n1, n2):
    total = n1 + n2
    return total

def subtract(n1, n2):
    total = n1 - n2
    return total

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1/n2

num1 = float(input("Number 1: "))
num2 = float(input("Number 2: "))
choice = int(input("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n>"))

if choice == 1:
    result = add(num1, num2)    
elif choice == 2:
    result = subtract(num1, num2)
elif choice == 3:
    result = multiply(num1, num2)
elif choice == 4:
    result = divide(num1, num2)
else:
    print("Invalid input")

print(f'Result: {result}')