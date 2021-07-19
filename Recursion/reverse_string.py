# Exercise problem C-4.16
def reverse_string(S):
    if len(S) == 0:
        return S
    else:
        return reverse_string(S[1:]) + S[0]

print(reverse_string("lalal"))
