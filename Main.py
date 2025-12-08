from SortingAlgorithms import bubbleSort, quicksort, mergesort
from random import randint
import time
import numpy as np
import matplotlib.pyplot as plt

def timeComplexity(function, array):
    data = array.copy()
    start = time.time()
    data = function(data)
    end = time.time()

    total_time = end - start

    return total_time

bubbleEff = []
quickEff = []
mergeEff = []

for i in range(10):
    randArray = []
    array_size = randint(100,10000)
    i = 0
    while i < array_size:
        random_number = randint(0,10000)
        randArray.append(random_number)
        i += 1

    #print(f'Array Size is {array_size}!')
    #print('\n')

    time_quick = timeComplexity(quicksort, randArray)
    time_merge = timeComplexity(mergesort, randArray)
    time_bubble = timeComplexity(bubbleSort, randArray)

    quickEff.append(time_quick)
    mergeEff.append(time_merge)
    bubbleEff.append(time_bubble)


avg_quick = np.mean(quickEff)
avg_merge = np.mean(mergeEff)
avg_bubble = np.mean(bubbleEff)

print("Average Quicksort Time:", avg_quick)
print("Average Merge Sort Time:", avg_merge)
print("Average Bubble Sort Time:", avg_bubble)

plt.figure(figsize=(10,6))


plt.plot(range(1, 11), quickEff, 'o-', label='Quicksort')
plt.plot(range(1, 11), mergeEff, 's-', label='Merge Sort')
plt.plot(range(1, 11), bubbleEff, '^-', label='Bubble Sort')

plt.xlabel('Trial')
plt.ylabel('Time (seconds)')
plt.title('Sorting Algorithm Time over 10 Random Trials')
plt.legend()
plt.grid(True)
plt.show()






