from stack import Stack
my_stack = Stack()
my_stack.push(1)
my_stack.push(2)

for i in range(3):
    print("Attempting to pop.")
    value = my_stack.pop()
    print("Value returned:", value)

