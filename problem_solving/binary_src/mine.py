def b_search(arr, n):
    if len(arr) == 0: return None
    if arr[0] == n: return 0
    left, right = 0, len(arr) - 1
    
    while (right - left) >= 0:
        mid = (left + right) // 2
        x = arr[mid]
        if x is n: return mid
        elif x < n: left = mid + 1
        else: right = mid - 1
    return None

arr = [1,2,3,4,5,6,7,8,9]
cases = ((4, 3), (5, 4), (6, 5), (1, 0), (90, None))
for val, idx in cases:
    assert b_search(arr, val) == idx
print("ok")
