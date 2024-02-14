import sys
sys.stdin = open("./input.txt", "r")
T = int(input())


def solution(case):
    visited = [0] * 201
    for item in case:
        start = (item[0]+1) // 2
        end = (item[1]+1) // 2
        for num in range(start, end+1):
            visited[num] += 1
    return max(visited)


for tc in range(1, T+1):
    N = int(input())
    case_list = [list(sorted(map(int, input().split()))) for _ in range(N)]
    print(f'#{tc} {solution(case_list)}')