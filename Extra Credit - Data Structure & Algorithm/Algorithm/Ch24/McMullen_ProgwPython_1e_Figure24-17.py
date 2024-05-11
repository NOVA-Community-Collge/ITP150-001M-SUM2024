import random
 
def merge(items, left, middle, right):
    # Create enough storage to merge the two sections of the items array
    storage = [None for x in range(right - left + 1)]
    
    # Three indexes to keep track of the place in the left section,
    # right section, and merged storage.
    left_index = left
    right_index = middle + 1
    storage_index = 0
 
    # While there is something in both the left and right sections
    while left_index <= middle and right_index <= right:
        # If the left section has a number smaller than the right section
        # copy it over to the storage
        if items[left_index] <= items[right_index]:
             storage[storage_index] = items[left_index]
             storage_index += 1
             left_index += 1
        # Otherwise copy the number from the right section to storage
        else:
             storage[storage_index] = items[right_index]
             storage_index += 1
             right_index += 1
 
    # Check to see if there are any numbers in the left section and
    # copy them over
    # Numbers would only be in the left section if the right section ran out
    while left_index <= middle:
        storage[storage_index] = items[left_index]
        storage_index += 1
        left_index += 1
    
    # Check to see if there are any numbers in the right section
    # and copy them over
    # Numbers would only be in the right section if the left section ran out
    while right_index <= right:
        storage[storage_index] = items[right_index]
        storage_index += 1
        right_index += 1
    
    # Copy the merged numbers back into the correct place in the items array.
    for i in range(left, right + 1):
        items[i] = storage[i - left]
 
def merge_recurse(items, left, right):
    # If the left and right indexes pass each other it is the base case
    if left >= right:
        return
    
    # Find the middle
    middle = (left + right) // 2
    
    # Recurse left and right
    merge_recurse(items, left, middle)
    merge_recurse(items, middle + 1, right)
    
    # Merge the sorted left and right sections
    merge(items, left, middle, right)    
 
def merge_sort(items):
    # Start the recursion with all valid indexes
    # (length - 1 instead of length)
    merge_recurse(items, 0, len(items)-1)
            
if __name__ == '__main__':
    # Create the numbers 1 through 11 and shuffle them
    items = list(range(1,11))
    random.shuffle(items)
    
    # Test quick sort
    print("Items before Merge Sort:")
    print(items)
    
    merge_sort(items)
    
    print("Items after Merge Sort:")
    print(items)