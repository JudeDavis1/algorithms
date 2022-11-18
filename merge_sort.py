import random


def main():
    l = list(range(1, 10))
    random.shuffle(l)
    merge_sort(l)


def merge_sort(arr):
    if len(arr) <= 1:
        return
    
    # Find midpoint
    mid = len(arr) // 2
    L = arr[:mid]
    R = arr[mid:]
    
    # Sort Left and Right
    merge_sort(L)
    merge_sort(R)

    # Sort in-place so that we don't have to return anything.

    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1  # Move onto the next item if it is less that the right side.
        else:
            arr[k] = R[j]
            j += 1  # Same here
        k += 1
    
    # Pick up remaining elements in L or R
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
    
    print(arr)


if __name__ == '__main__':
    main()





