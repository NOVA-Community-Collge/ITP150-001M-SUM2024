import math

def factorial(n):
    print("My Special Factorial")
    total = 1
    for i in range(1, n+1):
        total *= i
    return total

print(math.factorial(5))
print(factorial(5))