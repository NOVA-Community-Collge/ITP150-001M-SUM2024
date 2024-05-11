import random
 
def bubble_sort(items):
    # Do n passes
    for i in range(len(items)):
    
        # Keep track of how many swaps for early exit
        swaps = 0
        
        # Look at each item except the last items that would be sorted
        # (i items)
        for j in range(len(items)-1-i):
            # If two items are out of place, swap them
            if items[j] > items[j+1]:
                items[j+1], items[j] = items[j], items[j+1]        
                swaps += 1
                
        # If no swaps happened during a pass, you can stop early
        if swaps == 0:
            break
            
if __name__ == '__main__':
    # Create the numbers 1 through 11 and shuffle them
    items = list(range(1,11))
    random.shuffle(items)
    
    # Test bubble sort
    print("Items before Bubble Sort:")
    print(items)
    
    bubble_sort(items)
    
    print("Items after Bubble Sort:")
    print(items)