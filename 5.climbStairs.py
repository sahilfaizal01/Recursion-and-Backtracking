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

# Method - 3 (Dynamic Programming)
def climbStairsDp(n):
    if n<=2:
        return n
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
print(climbStairsDp(5))
