import sys
sys.stdin = open("./input.txt", "r")
T = int(input())


def solution():
    visited = [0] * 401
    for item in case_list:
        if item[0] % 2 == 0:
            visited[item[0] - 1] = 1
        if item[1] % 2 == 1:
            visited[item[1] + 1] = 1

        for num in range(item[0], item[1] + 1):
            visited[num] += 1
    return max(visited)

for tc in range(1, T + 1):
    N = int(input())
    case_list = [list(sorted(map(int, input().split()))) for _ in range(N)]
    print(f'#{tc} {solution()}')
