import sys
sys.stdin = open("./input.txt", "r")
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    for row in range(-N, N+1):
        for col in range(-N, N + 1):
            if row**2 + col**2 <= N**2:
                cnt += 1
    print(f'#{tc} {cnt}')