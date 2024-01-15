import sys
sys.stdin = open("./SW Expert Academy/input.txt", "r")

T = int(input())

for _ in range(T):
    N = int(input())
    matrix = [[0 for _ in range(11)] for _ in range(11)]
    for count in range(N):
        x1, y1, x2, y2, color = list(map(int,input().split()))
        
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if not matrix[i][j]:
                    matrix[i][j] = color
                else:
                    matrix[i][j] = 3
    result = 0          
    for i in range(11):
        for j in range(11):
            if matrix[i][j] == 3:
                result += 1
    print(f'#{_ + 1} {result}')

    