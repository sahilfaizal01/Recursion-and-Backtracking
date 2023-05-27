# Method - 1
def climbStairs(n):
    if n == 1 or n == 2:
        return n
    return climbStairs(n-1) + climbStairs(n-2)

print(climbStairs(5))

# Method - 2 (More time efficient)
def climb(n):
    memo = {}
    memo[1] = 1
    memo[2] = 2
    if n in memo:
        return memo[n]
    else:
        memo[n] = climb(n-1) + climb(n-2)
        return memo[n]
print(climb(5))
