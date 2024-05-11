from node import Node
        
class Queue():    
    def __init__(self):
        self.front = None
        self.rear = None
        
    def enqueue(self, data):
        temp = Node(data)
        if self.rear == None:
            self.front = self.rear = temp
        else:
            self.rear.next = temp
            self.rear = temp
            