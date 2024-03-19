import sys
input = sys.stdin.readline

N = int(input())

case_list = [int(input()) for _ in range(N)]
dp = [( case_list[i] ,0) for i in range(N)]
print(dp)

for num in range(N-1, 1, -1):
    # 4
    if dp[num-1][1] == 1:
        dp[num-1] = (max(dp[num-1][0], dp[num][0] + case_list[num-1]), 1)
    dp[num-2] = (max(dp[num-2][0], dp[num][0] + case_list[num-2]), 0)

    print(num, dp)
    # print('df', dp[num-1], dp[num-2])