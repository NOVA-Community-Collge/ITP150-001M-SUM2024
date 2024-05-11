import random

def partition(items, left, right):
    # Pick the middle item to be the pivot value and move it out of the way
    middle = (left + right) // 2
    pivot = items[middle]
    items[middle], items[right] = items[right], items[middle]
    
    # Keep track of the boundary index
    boundary = left
    
    # Look at all other items
    for index in range(left, right):
        # If the item is less than the pivot then the boundary has to move
        if items[index] < pivot:
        
        # Swap with the current boundary value and increase boundary by 1
            items[index], items[boundary] = items[boundary], items[index]            
            boundary += 1
            
    # Move pivot to between the two groups of numbers as indicated by
    # the boundary index
    items[right], items[boundary] = items[boundary], items[right]
    
    # Return the boundary to inform quicksort how to recurse
    return boundary

def quick_recurse(items, left, right):
    # Check for base case
    # Did the left and right boundaries pass each other? Then stop.
    if left >= right:
        return
    
    # Find the pivot's position after partitioning
    pivot_position = partition(items, left, right)
    
    # Recurse left and right of pivot
    quick_recurse(items, left, pivot_position - 1)
    quick_recurse(items, pivot_position + 1, right)

def quick_sort(items):
    # Start the recursion to include all valid indexes
    # (length - 1 instead of length)
    quick_recurse(items, 0, len(items) - 1)
            
if __name__ == '__main__':
    # Create the numbers 1 through 11 and shuffle them
    items = list(range(1,11))
    random.shuffle(items)
    
    # Test quick sort
    print("Items before Quick Sort:")
    print(items)
    
    quick_sort(items)
    
    print("Items after Quick Sort:")
    print(items)