# Exercise problem R-4.6
def harmonic(n):
    if n == 1:
        return 1
    else:
        return harmonic(n-1) + 1/(n)

print(harmonic(5))
