from node import Node
        
class Stack():
    def __init__(self):
        self.top = None

    def __str__(self):
        string = "Top of stack - "
        traverser = self.top
        while traverser != None:
            string += str(traverser.data) + " "
            traverser = traverser.next
        
        string += " - Bottom of stack"
        
        return string

    def push(self, data):
        temp = Node(data)
        temp.next = self.top
        self.top = temp

    def pop(self):
        if self.top == None:
            print("Empty stack.")
        else:
            temp = self.top
            self.top = self.top.next
            return temp.data
