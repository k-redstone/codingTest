import sys, heapq
from collections import defaultdict
input = sys.stdin.readline


def solution(heap, item):

    while item == 0:
        item = heapq.heappop(heap)
    return item

T = int(input().rstrip())

for _ in range(T):
    k = int(input().rstrip())
    length = 0
    min_hq = []
    max_hq = []
    num_dict = defaultdict(int)
    for __ in range(k):
        method, num = input().rstrip().split()
        if method == 'I':
            heapq.heappush(min_hq, int(num))
            heapq.heappush(max_hq, (-int(num), int(num)))
            num_dict[int(num)] += 1
            length += 1
            continue
        elif method == 'D':
            if length == 0:
                continue
            elif num == '1':
                if max_hq:
                    pop_item = heapq.heappop(max_hq)
                    # print(pop_item)
                    while max_hq and num_dict[pop_item[1]] == 0:
                        pop_item = heapq.heappop(max_hq)
                    num_dict[pop_item[1]] -= 1
                    length -= 1
            else:
                if min_hq:
                    pop_item = heapq.heappop(min_hq)
                    while min_hq and num_dict[pop_item] == 0:
                        pop_item = heapq.heappop(min_hq)
                    num_dict[pop_item] -= 1
                    length -= 1
        # print(num_dict)
    if length == 0:
        print('EMPTY')
    else:
        num_list = list(filter(lambda v: v[1] != 0, num_dict.items()))
        # print(num_list)
        # max_num, min_num = heapq.heappop(max_hq), heapq.heappop(min_hq)
        print(max(num_list, key=lambda x : x[0])[0], min(num_list, key=lambda x : x[0])[0])