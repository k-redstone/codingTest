import sys
from collections import deque
input = sys.stdin.readline

def bfs(row, col, size):
    visited = [[0]*N for _ in range(N)]
    queue = deque([(row, col)])
    eat_list = []
    while queue:
        row, col = queue.popleft()

        for num in range(4):
            new_row, new_col = row + d_row[num], col + d_col[num]
            # 범위 안에 있고, 안간곳
            if 0 <= new_row < N and 0 <= new_col < N and visited[new_row][new_col] == 0:
                # 해당위치가 0이 아니고, 상어 사이즈가 물고기보다 크면 -> 먹을 수 있는 곳이면
                if case_matrix[new_row][new_col] != 0 and size > case_matrix[new_row][new_col]:
                    visited[new_row][new_col] = visited[row][col] + 1
                    eat_list.append((visited[new_row][new_col], new_row, new_col))
                # 움직일 위치가 빈공간이면 방문
                elif case_matrix[new_row][new_col] == 0:
                    visited[new_row][new_col] = visited[row][col] + 1
                    queue.append((new_row, new_col))
                # 상어 크기가 물고기랑 똑같으면 방문
                elif size == case_matrix[new_row][new_col]:
                    visited[new_row][new_col] = visited[row][col] + 1
                    queue.append((new_row, new_col))
    '''
    먹는 조건 
    1. 최단거리
    2. 가장위 -> row가 작은 쪽
    3. 가장 왼쪽 -> col이 작은쪽
    '''
    return sorted(eat_list, key= lambda item: (item[0], item[1], item[2]))



N = int(input())
case_matrix = [list(map(int, input().split())) for _ in range(N)]
d_row, d_col = [1, -1, 0, 0], [0, 0, -1, 1]
baby_shark = 2
eat = 0

for row in range(N):
    for col in range(N):
        if case_matrix[row][col] == 9:
            start_row, start_col = row, col
            # 처음위치 초기화를 안했네....
            case_matrix[row][col] = 0
            break

timer = 0
while True:
    eat_list = bfs(start_row, start_col, baby_shark)
    if not eat_list:
        break
    timer += eat_list[0][0]
    start_row, start_col = eat_list[0][1], eat_list[0][2]
    eat += 1
    case_matrix[start_row][start_col] = 0
    if baby_shark == eat:
        eat = 0
        baby_shark += 1

print(timer)
