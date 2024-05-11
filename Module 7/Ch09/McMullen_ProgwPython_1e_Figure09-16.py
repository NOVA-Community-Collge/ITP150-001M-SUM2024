external = 1
 
def example():
    internal = 2
    print("Internal inside function:", internal)
    external = 5
    print("External inside function:", external)
 
example()
print("External outside function:", external)
