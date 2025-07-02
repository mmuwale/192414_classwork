# Factorial of a number using iteration
n = int(input("Enter a number: "))
factorial : int = 1
if n >= 1:
    for i in range(1, n+1):
        factorial *= i
print("Factorial number is: ",factorial)

# Factorial of a number using recursion
def factorial(n:int) -> int:
    if n == 0 | n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(4))

# Power of a number using iteration
"""Creating a function that returns the power of a Number
It accepts Number, and exponent values as parameters."""
def findPower(number:int, exponent:int) -> int:
    resultPower = 1 # initialising resultPower to 1
    for i in range(1, exponent+1): # traversing in the range from 1 to given exponent+1
        resultPower *= number
    return resultPower # returning the resultPower

# Power of a number using recursion
def power(base:int, exp:int) -> int:
    if (exp == 1):
        return base
    if (exp != 1):
        return base * power(base, exp - 1)
base = int(input("Enter base: "))
exp = int(input("Enter exponential value: "))
print("Result:", power(base, exp))

# Fibonacci series using iteration
n_terms = int(input("How many terms the user wants to print? "))
n_1 = 0
n_2 = 1
count = 0
if n_terms <= 0: # check if the number of terms is valid
    n_terms = int(input("Invalid number, please enter a positive integer"))
elif n_terms == 1: # if the number of terms is 1
    print("Fibonacci sequence upto", n_terms, ":")
    print(n_1)
else:
    print("Fibonacci sequence:")
    while count < n_terms:
        print(n_1)
        nth = n_1 + n_2
        n_1 = n_2
        n_2 = nth
        count += 1

# Fibonacci series using recursion
def fibonacci_of(n:int) -> int:
    if n in {0, 1}: # base case
        return n
    else:
        return fibonacci_of(n - 1) + fibonacci_of(n - 2)

[fibonacci_of(i) for i in range(10)] # printing the first 10 Fibonacci numbers