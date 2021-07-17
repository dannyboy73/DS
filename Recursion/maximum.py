def maximum(S, length):
    if length == 1:      
        return S[0]
        
    return max(maximum(S, length-1), S[length-1])

print(maximum([2,6,8,4,1], 5))
