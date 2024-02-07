import sys
sys.stdin = open("./input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    A, B = input().split()
    cnt = pos = 0
    while pos < len(A):
        pos = A.find(B, pos)
        if pos == -1:
            break
        else:
            cnt += 1
            pos += len(B)
    cnt = cnt + len(A) - (len(B)*cnt)
    print(f'#{tc} {cnt}')
