import sys

sys.stdin = open("./input.txt", "r")
T = int(input())


def recurve(num):
    if num > 2 and memo[num] == 0:
        memo[num] = 2*(recurve(num-2)) + recurve(num-1)
    return memo[num]

def dp(num):
    for idx in range(3, num+1):
        memo[idx] = (2*memo[idx-2]) + memo[idx-1]
    return memo[num]

for tc in range(1, T+1):
    N = int(input()) // 10
    memo = [0]*(N+1)
    memo[1] = 1
    memo[2] = 3
    print(f'#{tc} {recurve(N)}')
