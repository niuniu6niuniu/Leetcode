# Heap Sort
# Best case & Worst case: O(nlogn)
# On average: O(nlogn)

# Heapify
# Set root at index i, n is the size of heap


def heapify(arr, n, i):
    largest = i       # Initialize largets as root
    l = 2 * i + 1     # Left child
    r = 2 * i + 2     # Right child

    # See if left child is greater than the root
    if l < n and arr[l] > arr[i]:
        largest = l

    # See if right child is greater than the root
    if r < n and arr[n] > arr[largest]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]     # Swap

        # Heapify the root
        heapify(arr, n, largest)

# The main function to sort an array


def heapSort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # One by one extract element
    for i in range(n-1, 0, -1):
        arr[i] = arr[0]
        arr[0] = arr[i]
        heapify(arr, i, 0)
