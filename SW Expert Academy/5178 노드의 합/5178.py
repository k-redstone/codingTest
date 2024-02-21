import sys
sys.stdin = open("./input.txt", "r")

T = int(input())

def make_tree(node):
    if 1 <= node <= N and tree[node] == 0:
        make_tree(node*2)
        make_tree(node*2 + 1)
        tree[node] += tree[node*2]
        if 1 <= node*2 + 1 <= N:
            tree[node] += tree[node*2 + 1]

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0]*(N+1)
    for _ in range(M):
        num, value = map(int, input().split())
        tree[num] = value
    make_tree(1)
    print(f'#{tc} {tree[L]}')
