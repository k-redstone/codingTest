import sys
from collections import deque, defaultdict
sys.stdin = open("./input.txt", "r")

def solution(cur_arr, next_arr, max_num):
    while cur_arr:
        pop_item = cur_arr.popleft()
        for item in graph[pop_item]:
            if item not in visit:
                visit.add(item)
                next_arr.append(item)
    if len(cur_arr) == 0 and len(next_arr) == 0:
        return max_num
    return solution(next_arr, cur_arr, max(next_arr))

for tc in range(1, 11):
    N, start_node = map(int, input().split())
    case_list = list(map(int, input().split()))
    graph = defaultdict(list)
    visit = {start_node, }
    for idx in range(0, N, 2):
        graph[case_list[idx]].append(case_list[idx+1])
    cur_call = deque(graph[start_node])
    next_call = deque()
    result = solution(cur_call, next_call, max(cur_call))
    print(f'#{tc} {result}')