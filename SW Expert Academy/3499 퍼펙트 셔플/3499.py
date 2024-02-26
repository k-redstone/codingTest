import sys
sys.stdin = open("./input.txt", "r")
T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=" ")
    N = int(input())
    case_list = list(input().split())
    start = 0
    end = time = (len(case_list) // 2 if len(case_list) % 2 == 0 else len(case_list) // 2 + 1)
    for _ in range(time):
        print(case_list[start], end=" ")
        if end < N:
            print(case_list[end], end=" ")
            end += 1
        start += 1
    print()
