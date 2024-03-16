import sys
input = sys.stdin.readline

def solution(n):
    dp = [0]*(n+1)
    if n ==1 :
        return 1
    if n == 2:
        return 2
    if n >= 3:
        dp[1] = 1
        dp[2] = 2
        for idx in range(3, n+1):
            dp[idx] = (dp[idx-1] + dp[idx-2]) % 10007
    return dp[n]
result = solution(int(input().rstrip()))

print(result)