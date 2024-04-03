import sys
from collections import deque
input = sys.stdin.readline



def BFS(row, col):
    # Que 생성 후 방문 했다는 표시로 2지정
    Q = deque()
    Q.append((row, col))
    case_matrix[row][col] = 2
    while Q:
        row, col = Q.popleft()
        # 델타 탐색
        for n_row, n_col in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
            # 좌표 범위 넘아갔는지 확인
            if 0 <= n_row < N and 0 <= n_col < M:
                # 방문안한 배추라면
                if case_matrix[n_row][n_col] == 1:
                    # 방문했다고 바꾸고 큐에 좌표 넣기
                    case_matrix[n_row][n_col] = 2
                    Q.append((n_row, n_col))

    return 1


# 테케 갯수
T = int(input().rstrip())
for _ in range(T):
    # 인풋 받기
    M, N, K = map(int, input().rstrip().split())
    # 초기화된 행렬 생성
    case_matrix = [[0]*M for _ in range(N)]
    # 행렬에 배추 심기
    for _ in range(K):
        col, row = map(int, input().rstrip().split())
        case_matrix[row][col] = 1

    answer = 0

    for row in range(N):
        for col in range(M):
            # 배추가 심어져있다면
            if case_matrix[row][col] == 1:
                # BFS실행
                answer += BFS(row, col)
    print(answer)
