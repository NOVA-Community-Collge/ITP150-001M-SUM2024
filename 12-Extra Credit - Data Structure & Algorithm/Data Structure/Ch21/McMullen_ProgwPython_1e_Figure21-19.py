class Stack():
    def __init__(self):
        self.contents = []
        
    def push(self, data):
        self.contents.append(data)

    def pop(self):
        if len(self.contents) == 0:
            print("Empty Stack")
        else:
            return self.contents.pop(-1)

    def __len__(self):
        return len(self.contents)
        
class Queue():    
    def __init__(self):
        self.contents = []
         
    def enqueue(self, data):
        self.contents.append(data)
        
    def dequeue(self):
        if len(self.contents) == 0:
           print("Empty queue.")
        else:
            return self.contents.pop(0)
       
    def __len__(self):
        return len(self.contents)


if __name__ == '__main__':
    s = Stack()
    q = Queue()
    s.push(4)
    s.push(2)
    s.push(3)
    print(s.contents)
    print(s.pop())
    q.enqueue(4)
    q.enqueue(2)
    q.enqueue(3)
    print(q.contents)
    print(q.dequeue())
    