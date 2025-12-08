def bubbleSort(array):
    n = len(array)
    
    for i in range(n):
        swapped = False
        
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        
        if not swapped:
            break
    
    return array

def quicksort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[-1]
    left = [x for x in array[:-1] if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array[:-1] if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)

def mergesort(array):
    if len(array) <= 1:
        return array
    
    # Divide
    mid = len(array) // 2
    left = mergesort(array[:mid])
    right = mergesort(array[mid:])
    
    # Merge
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

