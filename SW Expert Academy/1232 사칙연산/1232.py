import sys
sys.stdin = open("./input.txt", "r")

def calc(root, left, right):
    if root == '+':
        return tree[left][0] + tree[right][0]
    if root == '-':
        return tree[left][0] - tree[right][0]
    if root == '*':
        return tree[left][0] * tree[right][0]
    if root == '/':
        return tree[left][0] / tree[right][0]

def travel(node):
    if tree[node][1] != 0:
        travel(tree[node][1])
        travel(tree[node][2])
        tree[node][0] = calc(tree[node][0], tree[node][1], tree[node][2])

for tc in range(1, 11):
    N = int(input())
    tree = dict()

    for _ in range(N):
        node_info = list(input().split())
        if len(node_info) == 4:
            tree[int(node_info[0])] = [node_info[1], int(node_info[2]), int(node_info[3])]
            continue
        tree[int(node_info[0])] = [int(node_info[1]), 0, 0]
    travel(1)
    print(f'#{tc} {int(tree[1][0])}')