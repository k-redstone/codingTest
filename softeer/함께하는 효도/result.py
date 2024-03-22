import sys
import copy
# input = sys.stdin.readline
sys.stdin = open("./softeer/함께하는 효도/input.txt", "r")


def back(point, cnt, visit, sum_num):
    global temp_matrix
    global max_sum
    if cnt >= 3:
        if sum_num > max_sum:
            max_sum = sum_num
            temp_matrix = copy.deepcopy(case_matrix)
            for item in visit:
                row, col = item
                temp_matrix[row][col] = 0
        return

    row, col = point
    for n_row, n_col in [ (row+1 , col),(row-1 , col),(row , col+1),(row, col-1)]:
        if 0 <= n_row < N and 0 <= n_col < N:
            if (n_row, n_col) not in visit:
                visit.add((n_row, n_col))
                back((n_row, n_col), cnt+1, visit, sum_num + case_matrix[n_row][n_col])
                visit.remove((n_row, n_col))

N, M = map(int, input().rstrip().split())

case_matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]
people_list = [list(map(int, input().rstrip().split())) for _ in range(M)]
max_sum = 0
temp_matrix = []


for people in people_list:
    max_sum += case_matrix[people[0]-1][people[1]-1]
    case_matrix[people[0]-1][people[1]-1] = 0

visit = set()
for people in people_list:
    print('asdfsadf')
    visit.add((people[0]-1, people[1]-1))
    back((people[0]-1, people[1]-1), 0, visit, max_sum)
    visit.clear()
    case_matrix = copy.deepcopy(temp_matrix)
    print(case_matrix)

print(max_sum)
