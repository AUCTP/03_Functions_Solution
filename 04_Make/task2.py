'''
In this make task, we will write a function calculating the factorial of a number given as input. 
The factorial of a number is the product of all the integers from 1 to that number (e.g. 5! = 5*4*3*2*1, ...). 
Hint: You can use recursion to solve this task.

Bonus import the module time and use its ``time()``` function (```time.time()```) to determine how long your program takes to calculate the factorial.
'''
import time

def factorial(num):
    if num > 1:
        return num * factorial(num - 1)
    else:
        return 1
    
num = int(input("Number: "))
start = time.time()
result = factorial(num)
end = time.time()
print(f'{num}! = {result}. It took {end-start} seconds to calculate')

# Alternative ohne Rekursion
num = int(input("Number: "))
result = 1
for i in range(1, num + 1):
    result = result * i
print(f'{num}! = {result}')