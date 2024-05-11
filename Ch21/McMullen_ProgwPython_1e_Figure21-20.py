from node import Node
from linearStructures import Stack, Queue

def depth_first_traversal(tree):
    node_stack = Stack()
    node_stack.push(tree)
    
    while len(node_stack) > 0:
        visiting_node = node_stack.pop()
        print(visiting_node.data, end=" ")
        
        if visiting_node.right != None:
            node_stack.push(visiting_node.right)
        if visiting_node.left != None:
            node_stack.push(visiting_node.left)
            
    print()
    
    
    
def breadth_first_traversal(tree):
    node_queue = Queue()
    node_queue.enqueue(tree)
    
    while len(node_queue) > 0:
        visiting_node = node_queue.dequeue()
        print(visiting_node.data, end=" ")
        
        if visiting_node.right != None:
            node_queue.enqueue(visiting_node.right)
        if visiting_node.left != None:
            node_queue.enqueue(visiting_node.left)
            
    print()
    
    

if __name__ == '__main__':
    tree = Node(5)
    
    # Depth 1
    tree.left = Node(2)
    tree.right = Node(8)
    
    # Depth 2
    tree.left.left = Node(1)
    tree.left.right = Node(3)
    tree.right.left = Node(7)
    tree.right.right = Node(10)
    
    print(tree)
    
    depth_first_traversal(tree)
    breadth_first_traversal(tree)