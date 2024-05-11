from node import Node

class Stack():
    def __init__(self):
        self.top = None

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
