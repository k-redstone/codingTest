import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [num for num in range(N+1)]

# def find_root(num):
#     while num != graph[num]:
#         num = graph[num]
#     return num


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
    
for _ in range(M):
    method, a, b = map(int, input().split())
    if method == 0:
        sum_set(a, b)
    else:
        if find_root(a) == find_root(b):
            print('YES')
        else:
            print('NO')