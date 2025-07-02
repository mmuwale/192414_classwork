# 1. Write a Python program to count down numbers from n to 1 using a while loop
"""n = int(input("Enter a number: "))
while n > 0:
    print(n)
    n -= 1"""

# 2. Write a Python program to achieve the same as 1, i.e a recursive method that counts down numbers from n to 1
"""def countdown(n: int) -> None:
    if n > 0: # base case is when n = 0
        print(n)
        countdown(n - 1) # general case decrements n by 1

n = int(input("Enter a number: "))
countdown(n)"""

# 3. Write a Python program that uses a while loop to count down numbers within a range. The user should be asked to input the start and end
"""upper = int(input("Enter the upper end of the range: "))
lower = int(input("Enter the lower end of the range: "))
while upper >= lower:
    print(upper)
    upper -= 1"""

# 4. Write a Python program that achieves the same as 3, but using recursion
def countdown(upper: int, lower: int) -> None:
    if upper >= lower: # base case is when upper < lower
        print(upper)
        countdown(upper - 1, lower) # general case decrements upper by 1, but lower stays the same

upper = int(input("Enter the upper end of the range: "))
lower = int(input("Enter the lower end of the range: "))
countdown(upper, lower)