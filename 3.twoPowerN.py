def twoPowerN(n):
    if n == 1:
        return 2
    return 2 * twoPowerN(n-1)

print(twoPowerN(5))
