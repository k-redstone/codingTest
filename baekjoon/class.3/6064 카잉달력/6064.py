import sys
import math
input = sys.stdin.readline

def solution():
    cnt_x = 0
    while True:
        now = (M*cnt_x) + x
        if now < N:
            d_y = now
        elif now % N == 0:
            d_y = N
        else:
            d_y = now % N

        if d_y == y:
            return now
        
        if now > max_year:
            return -1
        cnt_x += 1

#  x < M 이면 x' = x + 1이고, 그렇지 않으면 x' = 1
T = int(input().rstrip())
for _ in range(T):
    M, N, x, y = map(int, input().rstrip().split())
    max_year = math.lcm(M, N)
    year = solution()
    print(year)
