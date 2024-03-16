import sys
sys.stdin = open("./SW Expert Academy/1952 수영장/input.txt", "r")


def solution(prices, plans):
    dp = [0] * 13  # dp[i]: i월까지의 최소 비용
    for i in range(1, 13):
        # 1일 이용권으로 이용하는 경우
        dp[i] = dp[i-1] + prices[0] * plans[i-1]

        # 1달 이용권으로 이용하는 경우
        if i >= 1:
            dp[i] = min(dp[i], dp[i-1] + prices[1])

        # 3달 이용권으로 이용하는 경우
        if i >= 3:
            dp[i] = min(dp[i], dp[i-3] + prices[2])

    # 1년 이용권으로 이용하는 경우
    dp[12] = min(dp[12], prices[3])

    return dp[12]

T = int(input())
for tc in range(1, T + 1):
    prices = list(map(int, input().split()))
    plans = list(map(int, input().split()))

    result = solution(prices, plans)
    print(f"#{tc} {result}")
