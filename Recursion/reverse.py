# pg. 171 reversing a list using recursion
def reverse(S, start, stop):
    '''Reverse elements in a list'''
    if start < stop-1:
        S[start], S[stop-1] = S[stop-1], S[start]
        reverse(S, start+1, stop-1)

    return S

print(reverse([1, 4, 5, 7, 2, 3], 0, 6))
