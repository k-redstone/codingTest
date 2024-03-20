import sys
sys.stdin = open("./input.txt", "r")


T = int(input())

def find_root(num):
    if num != graph[num]:
        graph[num] = find_root(graph[num])
    return graph[num]

def sum_set(a, b):
    root_a = find_root(a)
    root_b = find_root(b)
    if root_a < root_b:
        graph[root_b] = root_a
    else:
        graph[root_a] = root_b

for tc in range(1, T+1):
    N, M = map(int, input().split())
    case_list = list(map(int, input().split()))
    graph = [num for num in range(N + 1)]
    group = []
    for idx in range(0, M*2, 2):
        group.append((case_list[idx], case_list[idx+1]))

    for item in group:
        a, b = item
        sum_set(a, b)
    for num in range(1, N+1):
        graph[num] = find_root(num)

    print(f'#{tc} {len(set(graph)) - 1}')