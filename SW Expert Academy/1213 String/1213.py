import sys
sys.stdin = open('./input.txt', 'r', encoding='UTF8')

for tc in range(10):
    T = input()
    A = input()
    B = input()
    cnt = pos = 0
    while pos < len(B):
        pos = B.find(A, pos)
        if pos == -1:
            break
        cnt += 1
        pos += len(A)
    print(f'#{T} {cnt}')
    # print(f'#{T} {B.count(A)}')
