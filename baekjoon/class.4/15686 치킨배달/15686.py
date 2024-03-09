import sys
from itertools import combinations
input = sys.stdin.readline

def get_dist(pick_list, house):
    dist = 100
    for pick in pick_list:
        d = abs(pick[0]-house[0]) + abs(pick[1]-house[1])
        dist = min(dist, d)
    return dist

def get_total_dist(store):
    global answer
    total_num = 0
    for house in house_list:
        if total_num > answer:
            return
        total_num += get_dist(store, house)
    answer = min(answer, total_num)

def solution():
    for store in select_list:
        get_total_dist(store)

N, M = map(int, input().rstrip().split())
case_matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]
house_list = []
store_list = []

for row in range(N):
    for col in range(N):
        if case_matrix[row][col] == 1:
            house_list.append((row,col))
            continue
        if case_matrix[row][col] == 2:
            store_list.append((row,col))
            continue

select_list = list(combinations(store_list, M))
answer = 999999999
total_dist = 0
solution()
print(answer)