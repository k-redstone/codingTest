import sys
from collections import deque
input = sys.stdin.readline

def bfs(visited):
    while Q:
        row, col = Q.popleft()
        for idx in range(4):
            new_row, new_col = row+d_row[idx], col+d_col[idx]
            if 0 <= new_row < N and 0 <= new_col < N:
                if case_matrix[row][col] == case_matrix[new_row][new_col]:
                    if not visited[new_row][new_col]:
                        visited[new_row][new_col] = 1
                        Q.append((new_row, new_col))

N = int(input())
case_matrix = [list(input()) for _ in range(N)]
d_row, d_col = [0, 0, -1, 1], [-1, 1, 0, 0]
not_people = [[0]*N for _ in range(N)]
people = [[0]*N for _ in range(N)]
cnt_not = 0
cnt_ok = 0
for row in range(N):
    for col in range(N):
        if not not_people[row][col]:
            Q = deque([(row, col)])
            bfs(not_people)
            cnt_not +=1
        if case_matrix[row][col] == 'R':
            case_matrix[row][col] = 'G'
for row in range(N):
    for col in range(N):
        if not people[row][col]:
            Q = deque([(row, col)])
            bfs(people)
            cnt_ok +=1

print(cnt_not, cnt_ok)