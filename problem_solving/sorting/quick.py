def quick_lr(arr):
    def quick(arr, s, e):
        if s < e:
            mid = (s + e) // 2
            pivot = arr[mid]
            index = partition(arr,s,e,pivot)
            quick(arr, s, index - 1)
            quick(arr, index, e)

    def partition(arr, l, r, pivot):
        while l <= r:
            print(arr[l], pivot, arr[r])
            while arr[l] < pivot: l += 1
            while arr[r] > pivot: r -= 1
            if l <= r:
                arr[l], arr[r] = arr[r], arr[l]
                l+=1
                r-=1
        return l
    return quick(arr, 0, len(arr) - 1)

#print(partition([2,5,3,1,4]))
#print(partition([2,5,3,1,4]))
arr = [2,4,3,5,1]
print(quick_lr(arr), arr)

#print(partition(arr, 0, len(arr) - 1), arr)

def quick_rand(s):
    def quick(s, l, h):
        if h - l > 0:
            p = rand_partition(s, l, h)
            quick(s, l, p - 1)
            quick(s, p+1, h)

    def rand_partition(s, l, r):
        pivot = r
        firstHigh = l

        for i in range(l, r):
            if s[i] <= s[pivot]:
                s[i], s[firstHigh] = s[firstHigh], s[i]
                firstHigh += 1 
        s[pivot], s[firstHigh] = s[firstHigh], s[pivot]
        
        print(s)
        return firstHigh
        
    return quick(s, 0, len(s) - 1)
    #return rand_partition(s, 0, len(s) - 1)
s = [17, 12, 6, 19, 23, 8, 5, 10]
#print(rand_partition(s, 0, len(s) - 1), s)
print(s, quick_rand(s), s)

print("--------------------------- LOMUTO ---------------------------------")

def quick_lomuto(a):
    def quick(s, e):
        if s >= e: return
        idx = partition(a, s, e)
        quick(s, idx - 1)
        quick(idx + 1 , e)
        
    def partition(a, l, r):
        idx = l
        p = a[l]
        for i in range(l+1, r + 1):
            if a[i] < p:
                a[i], a[idx + 1] = a[idx + 1], a[i]
                idx += 1
        a[l], a[idx] = a[idx], a[l]
        return idx
    #return partition(a, 0, len(a) - 1)
    return quick(0, len(a) - 1)
a = [17, 12, 6, 19, 23, 8, 5, 10]
#print(rand_partition(s, 0, len(s) - 1), s)
print(a)
print(quick_lomuto(a), a)
