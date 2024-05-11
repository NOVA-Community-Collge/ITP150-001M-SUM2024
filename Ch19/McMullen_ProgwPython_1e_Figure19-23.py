from node import Node

class LinkedList():
    def __init__(self):
        self.head = None
        
    def insert(self, data, position):
        if position == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            
        else:
            temp = self.head
            while temp.next != None and position > 1:
                temp = temp.next
                position -= 1
            
            new_node = Node(data)
            new_node.next = temp.next
            temp.next = new_node    
    
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
    
    def __contains__(self, target):
        traverser = self.head
        while traverser != None:
            if traverser.data == target:
                return True
            traverser = traverser.next
        
        return False
                
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            searcher = self.head
            while searcher.next != None:
                searcher = searcher.next
            
            searcher.next = new_node
    