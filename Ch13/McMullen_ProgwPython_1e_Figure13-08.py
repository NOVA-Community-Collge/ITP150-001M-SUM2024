
pi = 3.14159

def abs(x):
    if x < 0:
        return -x
    else:
        return x

def factorial(n):
    total = 1
    for i in range(1, n+1):
        total *= i
    return total

def test():
    print("Testing math:")
    print("Absolute value of -5:", abs(-5))
    print("Absolute value of 5:", abs(5))
    print("Value of pi:", pi)
    print("Factorial of 5:", factorial(5))