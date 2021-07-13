# pg. 170 sum of first n numbers in a list
def linear_sum(S, n):
    if n == 0:
        return 0
    else:
        return linear_sum(S, n-1) + S[n-1]

print(linear_sum([3, 6, 9, 8, 2, 4, 7, 11], 8))
