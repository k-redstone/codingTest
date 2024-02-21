import sys
sys.stdin = open("./input.txt", "r")


def travel_in_order(node):
    global answer
    if node:
        travel_in_order(tree[node][1])
        answer += tree[node][0]
        travel_in_order(tree[node][2])

for tc in range(1, 11):
    N = int(input())
    tree = {i: [] for i in range(1, N+1)}
    answer = ''
    for _ in range(N):
        node_info = list(input().split())
        node = int(node_info[0])
        if len(node_info) == 4:
            tree[node].extend([node_info[1], int(node_info[2]), int(node_info[3])])
        if len(node_info) == 3:
            tree[node].extend([node_info[1], int(node_info[2]), 0])
        if len(node_info) == 2:
            tree[node].extend([node_info[1], 0, 0])
    travel_in_order(1)
    print(f'#{tc} {answer}')