def merge_sort(arr):
    if len(arr) in (0, 1):
        return arr
    mid = len(arr) // 2
    c = merge_sort(arr[0:mid])
    d = merge_sort(arr[mid:])
    return merge(c, d)
    #return [*c, *d]

def merge(c, d):
    b = []
    i, j, k = 0, 0, 0
    while i < len(c) and j < len(d): 
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


def merger(A, li, lj, ri, rj):
    while li < lj and ri < rj:
        if A[li] > A[ri]:
            A[li], A[ri] = A[ri], A[li]
            print(A[li])
            li += 1
        else:
            ri += 1


if __name__ == "__main__":
    a = [5,34,2,6,7,8,8,34,3]
    print(merge_sort(a))


#merge([1,2,3,34], [1,2,3,34,56])

#print("\n\n\n")
#merge([1, 3], [2, 2,3,10])
