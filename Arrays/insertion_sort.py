def insertion_sort(A):
    """Insertion sort to sort a list"""
    for k in range(1, len(A)):
        cur = A[k]
        j = k
        while j > 0 and A[j-1] > cur:
            A[j] = A[j-1]
            j -= 1

        A[j] = cur
    return A

print(insertion_sort([1, 9, 8, 3, 5, 6]))
