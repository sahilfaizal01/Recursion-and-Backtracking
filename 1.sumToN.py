def sumToN(n):
    if n == 1:
        return 1
    return sumToN(n-1) + n

print(sumToN(5))
