import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

def select(idx):
    if can_choose:
        pop_item = heapq.heappop(can_choose)
        carry_dict[idx] = pop_item[2]


def solution(hq):
    for idx, bag in enumerate(bag_list):
        while True:
            if len(hq) == 0:
                break
            M, V = heapq.heappop(hq)
            if bag < M:
                item = (M, V)
                heapq.heappush(hq, item)
                break
            heapq.heappush(can_choose, (-V, M, V))
        select(idx)


N, K = map(int, input().rstrip().split())
carry_dict = defaultdict(int)
item_list = [tuple(map(int, input().rstrip().split())) for _ in range(N)]


bag_list = list(sorted([int(input()) for _ in range(K)]))
heapq.heapify(item_list)

can_choose = []
result = 0
solution(item_list)
# print(carry_dict)
for value in carry_dict.values():
    if type(value) == int:
        result += value

print(result)