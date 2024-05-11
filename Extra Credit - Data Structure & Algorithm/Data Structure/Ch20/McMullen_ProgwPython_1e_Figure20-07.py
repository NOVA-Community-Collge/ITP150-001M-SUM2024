from node import Node

class Stack():
    def __init__(self):
        self.top = None
    
    def push(self, data):
        temp = Node(data)
        temp.next = self.top
        self.top = temp

