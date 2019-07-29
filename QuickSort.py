# QuickSort
# Worst case: O(n.^2)
# Average case: O(nlogn)

# Idea: Recursively select a Pivot, make the smaller elements to it's left
#       and the greater elements to the right.

# Start from low and end at high
def quicksort(arr, low, high):
    # if there is at least 2 elements in the array
    if low < high:
        # pi as Pivot
        pi = partition(arr, low, high)
        # Do quicksort on both smaller array and greater array
        quicksort(arr, low, pivot)
        quicksort(arr, pi + 1, high)
    return arr

def partition(arr, low, high):
    # Set the first element to be pivot
    pi = low
    # Create a border element start from the next element of the pivot
    border = low
    for i in range(low, high):
        if arr[i] <= arr[pi]:
            # Swap the smaller element with the border
            arr[i], arr[border] = arr[border], arr[i]
            border += 1
    # Swap pivot with border
    arr[pi], arr[border] = arr[border], arr[pi]
