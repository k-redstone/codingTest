import sys
from collections import deque
input = sys.stdin.readline


def BFS(point):
    Q = deque()
    Q.append(point)
    visit_set.add(point)
    while Q:
        row, col = Q.popleft()
        for n_row, n_col in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
            if (n_row, n_col) in case_set:
                if (n_row, n_col) not in visit_set:
                    visit_set.add((n_row, n_col))
                    Q.append((n_row, n_col))
    return 1


T = int(input().rstrip())
for _ in range(T):
    M, N, K = list(map(int, input().rstrip().split()))
    case_set = set(tuple(map(int, input().rstrip().split())) for _ in range(K))
    visit_set = set()
    answer = 0
    for point in case_set:
        if point not in visit_set:
            answer += BFS(point)
    print(answer)
