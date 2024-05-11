"""myMath.py
Author: Dr. Elizabeth Matthews

A module containing some math functions and
 an approximation of pi."""
 
pi = 3.14159

def abs(x):
    """abs(x)
    Returns the absolute value of x."""
    if x < 0:
        return -x
    else:
        return x

def factorial(n):
    """factorial(n)
    Returns the factorial of n."""
    total = 1
    for i in range(1, n+1):
        total *= i
    return total

def test():
    """A test program for the module."""
    print("Testing math:")
    print("Absolute value of -5:", abs(-5))
    print("Absolute value of 5:", abs(5))
    print("Value of pi:", pi)
    print("Factorial of 5:", factorial(5))

if __name__ == '__main__':
    test()