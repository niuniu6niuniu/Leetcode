# QuickSort
# Worst case: O(n.^2)
# Average case: O(nlogn)

# Keywords: 1. Recursive  2. Pivot  3. Border
# Idea: [ Smaller elements, Pivot, Greater elements ]
# Func 1: Apply Recursive 
# Func 2: Perform the compare and swap

# Start: low  End: high
def quicksort(arr, low, high):
    # More than 2 elements
    if low < high:
        # pi as Pivot
        pi = partition(arr, low, high)
        # Recursively apply on the sub-array
        quicksort(arr, low, pivot)
        quicksort(arr, pi + 1, high)
    return arr

def partition(arr, low, high):
    # Set the first element to be pivot
    pi = low
    # Make a border element next to pivot
    border = low
    for i in range(low, high):
        if arr[i] <= arr[pi]:
            # Swap the smaller element with the border
            arr[i], arr[border] = arr[border], arr[i]
            border += 1
    # Finally swap pivot with border
    arr[pi], arr[border] = arr[border], arr[pi]
