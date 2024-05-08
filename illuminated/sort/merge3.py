def merge3(A,B,C):
    i, j, k = 0, 0, 0

    res = []
    while i < len(A) and j < len(B) and k < len(C):
        if A[i] < B[j] and A[i] < C[k]:
            res.append(A[i])
            i+=1
        elif B[j] < C[k]:
            res.append(B[j])
            j+=1
        else:
            res.append(C[k])
            k += 1
    return res 


print(merge3([1,2,3,4], [7,8,9,10], [5,6,7,8]))

def sorted_array():
    return [1,2,3,4,5,6]
# Step 1: Start with k sorted arrays
k = 6  # Example value for k
arrays = [sorted_array() for _ in range(k)]  # Assuming sorted_array() returns a sorted array

# Step 2: Pair these arrays into k/2 pairs
k_half_pairs = []
for i in range(0, k, 2):
    if i + 1 < k:
        k_half_pairs.append((arrays[i], arrays[i+1]))
    else:
        # If k is odd, one array remains unpaired
        k_half_pairs.append((arrays[i], None))

# Displaying the arrays
print("Step 1: Start with k sorted arrays")
print(arrays)

print("\nStep 2: Pair these arrays into k/2 pairs")
print(k_half_pairs)

