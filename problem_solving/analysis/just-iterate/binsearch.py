import timeit
from matplotlib import pyplot
def linear(arr, n):
    i = 0;
    for i, x in enumerate(arr):
        if x  == n: return i
    return None
def binsearch(nums, n):
    lo, hi = 0, len(nums)
    while hi > lo:
        mid = (lo + hi) // 2   # still in range [lo, hi)
        x = nums[mid]
        if x == n:
            return mid
        if n < x:
            hi = mid
        if n > x:
            lo = mid + 1
    return None


if __name__ == '__main__':
    a = (0, 1, 3, 4)
    b = (-5, -2, 0)
    cases = (
        # find in any position, even size
        (a, 0, 0),
        (a, 1, 1),
        (a, 3, 2),
        (a, 4, 3),
        # find in any position, odd size
        (b, -5, 0),
        (b, -2, 1),
        (b, 0, 2),
        # fail to find
        (a, 2, None),
        (b, -3, None),
    )
    for nums, n, exp in cases:
        assert binsearch(nums, n) == exp
        assert linear(nums, n) == exp
    print('ok')

if __name__ == '__main__':
    num = 1 << 14
    ran =  num
    arr = []
    i = 0
    while i < num:
       arr.append(i) 
       i+=1
       
    bintiming = []
    lineartiming = []

    for x in range(0, ran):
        bintiming.append(timeit.timeit(lambda: binsearch(arr, x), number=3))
        lineartiming.append(timeit.timeit(lambda: linear(arr, x), number=3))

    pyplot.title("binary search vs linear search")
    pyplot.xlabel("number of items in array")
    pyplot.ylabel("time spent")
    pyplot.plot(arr, bintiming, lineartiming)
    pyplot.show(block=True)
