import matplotlib.pyplot as plt
from  merge import merge_sort
from random import random, shuffle
import timeit

arr = [int((random() * 100)) for _ in range(10000)]

merged = merge_sort(arr)
arr2 = [int((random() * 100)) for _ in range(10000)]


times = []
pytimes = []
for x in range(0, 500):
    a = arr[0:x]
    times.append(timeit.timeit(lambda: merge_sort(a), number=3))
    a = arr[0:x]
    pytimes.append(timeit.timeit(lambda: list(sorted(a)), number=3))

plt.title("binary search vs linear search")
plt.xlabel("number of items in array")
plt.ylabel("time spent")
plt.plot(arr[0:500],times, pytimes, label="test")
plt.show(block=True)
plt.show()

