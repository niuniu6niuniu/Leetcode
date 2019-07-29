# Merge Sort
# Worse/Best/Average case: O(nlogn)

# Idea: Divide & conquer
def merge_sort(arr):
    merge_sort2(arr, 0, len(arr)-1)

def merge_sort2(arr, first, last):
    # First element index of array
    # Last element index of array
    # If more than on element
    if first < last:
        middle = arr // 2
        # Recursively call mergetsort function
        merge_sort2(arr, first, last)
        merge_sort2(arr, first, last)
        # call merge function
        merge(arr, first, middle, last)

def merge(arr, first, middle, last):
    L = arr[first:middle]
    R = arr[middle:last+1]
    # Set a Big number as the stop sign
    L.append(999)
    R.append(999)
    i = j = 0
    for k in range(first, last+1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
