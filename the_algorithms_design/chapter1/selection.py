
def selec_sort(arr):
    for i in range(0,len(arr)):
        _min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[_min]: _min = j
        arr[_min], arr[i] = arr[i], arr[_min]
    return arr


print(selec_sort([10,1,5,10,4,7,8,9]))

