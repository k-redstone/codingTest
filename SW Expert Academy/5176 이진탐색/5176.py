import sys
sys.stdin = open("./input.txt", "r")

T = int(input())

def make(node):
    global num
    if 1 <= node <= N:
        make(node*2)
        num += 1
        tree[node] = num
        make(node*2 + 1)

for tc in range(1, T+1):
    N = int(input())
    tree = [0]*(N+1)
    num = 0
    make(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')