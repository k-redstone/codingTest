import sys
input = sys.stdin.readline

def solution(n, arr):
    if n == 1:
        return arr[0]
    if n == 2:
        return arr[0]+arr[1]
    dp = [0]*n
    dp[0] = arr[0]
    dp[1] = arr[0]+arr[1]
    dp[2] = max(arr[0] + arr[2], arr[1] + arr[2])

    for idx in range(3, n):
        dp[idx] = max(dp[idx-2] + arr[idx], dp[idx-3] + arr[idx-1] + arr[idx])
    return dp[n-1]

N = int(input())
case_list = [int(input()) for _ in range(N)]

result = solution(N, case_list)
print(result)