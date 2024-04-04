import sys
from collections import deque
input = sys.stdin.readline

def get_island(point, case_set):
    visited_set = set()
    visited_set.add(point)
    Q = deque([point])
    cnt = 1
    while Q:
        row, col = Q.popleft()
        for n_row, n_col in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
            if (n_row, n_col) not in visited_set and (n_row, n_col) in case_set:
                cnt += 1
                visited_set.add((n_row, n_col))
                Q.append((n_row, n_col))
    if len(case_set) == cnt:
        return True
    else:
        return False


def get_melting(point):
    row, col = point
    cnt = 0
    for n_row, n_col in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
        if case_matrix[n_row][n_col] == 0:
            cnt += 1
    return cnt


def solution():
    time = 1
    while case_set:
        melt_que = set()
        for island in case_set:
            cnt = get_melting(island)
            if cnt == 0:
                continue
            melt_que.add((island, cnt))
        for melting in melt_que:
            point, melt = melting
            if case_matrix[point[0]][point[1]] <= melt:
                case_matrix[point[0]][point[1]] = 0
                case_set.remove(point)
            else:
                case_matrix[point[0]][point[1]] -= melt
        for item in case_set:
            if not get_island(item, case_set):
                return time
            else:
                break
        time +=1 
    return 0


N, M = map(int, input().rstrip().split())

case_matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]
case_set = set()
for row in range(N):
    for col in range(M):
        if case_matrix[row][col] != 0:
            case_set.add((row, col))

print(solution())