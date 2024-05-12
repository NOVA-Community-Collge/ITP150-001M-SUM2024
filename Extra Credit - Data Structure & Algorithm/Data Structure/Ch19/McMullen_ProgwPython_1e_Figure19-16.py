from node import Node

class LinkedList():
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            searcher = self.head
            while searcher.next != None:
                searcher = searcher.next
            
            searcher.next = new_node