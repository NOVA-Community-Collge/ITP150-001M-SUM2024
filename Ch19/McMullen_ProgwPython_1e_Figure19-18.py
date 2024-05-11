from node import Node

class LinkedList():
    def __init__(self):
        self.head = None
    
    def __str__(self):
        string = ""
        if self.head == None:
            string += "The list is empty!"
        else:
            traverser = self.head
            while traverser != None:
                string += traverser.data + "\n"
                traverser = traverser.next
        
        return string
        
    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            searcher = self.head
            while searcher.next != None:
                searcher = searcher.next
            
            searcher.next = new_node
    