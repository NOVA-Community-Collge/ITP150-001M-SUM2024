def fibonacci(n):
    # Base case
    if n == 1 or n == 2:
        return 1
    
    # Find the fibonacci number for n - 1
    n1 = fibonacci(n - 1)
    
    # Find the fibonacci number for n - 2
    n2 = fibonacci(n - 2)
    
    # Add together and return
    return n1 + n2
 

n = int(input("Enter a number: "))
fibonacci_n = fibonacci(n)
print("The Fibonacci number is", fibonacci_n)
   




