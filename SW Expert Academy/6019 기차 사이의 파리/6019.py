import sys
sys.stdin = open("./input.txt", "r")
T = int(input())
for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())
    print(f'#{tc} {D*F /(A+B)}')