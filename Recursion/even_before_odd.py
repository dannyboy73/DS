# problem number C-4.19
def even_before_odd(S, n):
    if n == 0:
        return S

    elif S[n-1] % 2 == 0:
        x = S.pop(n-1)
        S.insert(0, x)

    else:
        x = S.pop(n-1)
        S.insert(n-1, x)

    return even_before_odd(S, n-1)

print(even_before_odd([9, 3, 6, 5, 2, 1], 6))
