from queue import Queue
my_queue = Queue()
my_queue.enqueue(1)
my_queue.enqueue(2)
print(my_queue)
print("Removing from queue:", my_queue.dequeue())
print("Removing from queue:", my_queue.dequeue())

