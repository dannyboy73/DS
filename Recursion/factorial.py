# example pg. 150
def factorial(n):
    if n == 0:  # base case     
        return 1
    else:
        return n * factorial(n-1)
