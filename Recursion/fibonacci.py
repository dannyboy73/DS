# pg. 167 fibonacci sum of nth term
def fibonacci(n):
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = fibonacci(n-1)
        return (a+b, a)

print(fibonacci(6)[0])
