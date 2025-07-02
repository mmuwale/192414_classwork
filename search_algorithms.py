# Linear Search
def linearSearch(array, n, x):
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1

# Binary Search - Iterative
def binarySearchIterative(array, x, low, high):
    # Repeat until the pointers low and high meet each other
    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Binary Search - Recursive
def binarySearchRecursive(array, x, low, high):
    if high >= low:
        mid = low + (high - low) // 2
        if array[mid] == x:
            return mid
        elif array[mid] > x:
            return binarySearchRecursive(array, x, low, mid-1)
        else:
            return binarySearchRecursive(array, x, mid+1, high)
    else:
        return -1