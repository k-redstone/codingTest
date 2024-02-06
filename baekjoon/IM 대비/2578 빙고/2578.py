import sys
sys.stdin = open("./baekjoon/IM 대비/2578 빙고/input.txt", "r")

matrix = [ list(map(int, sys.stdin.readline().split())) for i in range(5)]
print_number = []
for i in range(5):
    print_number.extend(list(map(int, sys.stdin.readline().split()))) 

row_list = [0]*5
col_list = [0]*5
cross = 0
recross = 0

def find(num):
    global cross
    global recross
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == num:
                row_list[row] += 1
                col_list[col] += 1
                if row == col:
                    cross += 1
                if row + col == 4:
                    recross += 1
                return True
    


for idx, number in enumerate(print_number):
    find(number)
    judge = 0
    judge +=row_list.count(5) + col_list.count(5)
    if cross == 5:
        judge += 1
    if recross == 5:
        judge += 1
    if judge >= 3:
        print(idx + 1)
        break
