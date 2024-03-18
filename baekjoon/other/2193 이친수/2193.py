import sys
input = sys.stdin.readline

def solution(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    dp = [0]*(n+1)
    dp[1], dp[2] = 1, 1

    for idx in range(2, n+1):
        dp[idx] = dp[idx-1] + dp[idx-2]

    return dp[n]


N = int(input().rstrip())

print(solution(N))
