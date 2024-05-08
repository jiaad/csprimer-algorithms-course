def merge_sort(arr):
    if len(arr) in (0, 1):
        return arr
    mid = len(arr) // 2
    c = merge_sort(arr[0:mid])
    d = merge_sort(arr[mid:])
    return merge(c, d)
    #return [*c, *d]

ttt = 0
def merge(c, d):
    b = []
    i, j, k = 0, 0, 0
    n = min(len(c), len(d))
    # while i < len(c) and j < len(d): 
    #print(i, n)
    while i < n and j < n:
        if c[i] < d[j]:
            b.append(c[i])
            i += 1
        else:
            b.append(d[j])
            j += 1
        k += 1
    while j < len(d):
        b.append(d[j])
        j += 1

    while i < len(c):
        b.append(c[i])
        i+=1
    return b


if __name__ == "__name__":
    a = [5,34,2,6,7,8,8,34,3]
#print(a)
    print(merge_sort(a))


#merge([1,2,3,34], [1,2,3,34,56])

#print("\n\n\n")
#merge([1, 3], [2, 2,3,10])
