from node import Node

def binary_search(tree, data):
    if tree == None:
        print("The item", data, "is NOT in the tree!")
    else:
        if tree.data == data:
            print("The item", data, "IS in the tree!")
        elif tree.data > data:
            binary_search(tree.left, data)
        else:
            binary_search(tree.right, data)

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
    
    binary_search(tree, 7)
    binary_search(tree, 3)
    binary_search(tree, 12)