def NthFibonacci(n):
    if n == 1 or n == 0:
        return n
    return NthFibonacci(n-1) + NthFibonacci(n-2)

print(NthFibonacci(9))
