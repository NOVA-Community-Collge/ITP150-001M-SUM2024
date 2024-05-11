class Node():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def print_tree(self, level=0):
        # Recursive string creation for a tree node
        # Prints the tree rotated 90 degrees to the left
        
        s = ""
        
        # If there is a right subtree, print it first
        if self.right != None:
            s += self.right.print_tree(level + 1)
            
        # Add space to the left before printing the current node's data
        for i in range(level):
            s += "| "
            
        s += str(self.data) + "\n"
        
        # If there is a left subtree, print it last
        if self.left != None:
            s += self.left.print_tree(level + 1)
            
        return s
    
    def __str__(self):
        # Override the print() dunder method
        return self.print_tree(0)

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