
arr = [5,34,2,6,7,8,8,34,3,5]
arr2 = arr.copy()
def merge_sort(nums):
    
    working = [0] * len(nums)

    def sort(left, right):
        if right - left in (0, 1):
            return 
        mid = (right + left) // 2
        sort(left, mid)
        sort(mid,right)
        return merge(left, mid, right)


    def merge(left, mid, right):
        sep = mid
        for i in range(left, right):
            working[i] = nums[i]
        #    
        #    li , ri = left, mid
        #    for i in range(left, right):
        #        if ri == right: # all element of the right is merged
        #            print(ri, right, A, i)
        #            A[i] = working[li]
        #            li+=1
        #        elif ((li < mid) and working[li] < working[ri]):
        #            A[i] = working[li]
        #            li+=1
        #        else:
        #            A[i] = working[ri]
        #            ri+=1
        #    print(A)
        #
        li, ri = left, mid 
        i = left
        while li < sep and ri < right:
            if working[li] < working[ri]:
                nums[i] = working[li]
                li += 1
            else:
                nums[i] = working[ri]
                ri += 1
            i += 1
        
        j = i
        while li < sep:
            nums[j] = working[li]
            li += 1
            j += 1
            
        while ri < right:
            nums[i] = working[ri]
            ri += 1
            i += 1
        return nums    
    return sort(0, len(nums))


if __name__ == "__main__":
    a = [4,5,6,7,8,9 ,1,2,3,4,5,6]
    merge_sort(arr)
    print(arr, arr2, a)
    assert sorted(arr2) == arr
    print("ok")