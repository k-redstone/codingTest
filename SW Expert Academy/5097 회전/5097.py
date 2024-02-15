import sys
sys.stdin = open("./input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    case_list = list(map(int, input().split()))
    print(f'#{tc} {case_list[M%N]}')