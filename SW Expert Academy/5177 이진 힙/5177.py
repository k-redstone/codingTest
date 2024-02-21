import sys
sys.stdin = open("./input.txt", "r")

T = int(input())

def enq(node):
    global last
    last += 1
    tree[last] = node
    child = last
    parent = child // 2
    while parent >= 1 and tree[parent] > tree[child]:
        tree[parent], tree[child] = tree[child], tree[parent]
        child = parent
        parent = child // 2

for tc in range(1, T+1):
    N = int(input())
    case_list = list(map(int, input().split()))
    tree = [0]*(N+1)
    last = 0
    for item in case_list:
        enq(item)
    node = last // 2
    sum_num = 0
    while node >= 1:
        sum_num += tree[node]
        node = node // 2
    print(f'#{tc} {sum_num}')