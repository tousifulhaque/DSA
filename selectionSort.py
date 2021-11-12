A = [1024, 352, 332, 351,33, 2, 1, 39] # n space complexity

for i in range(len(A)):

    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j

    A[i], A[min_idx] = A[min_idx], A[i]

print('Sorted Array')
for i in range(len(A)):
    print(A[i])
