import sys
sys.stdin = open("./baekjoon/IM 대비/2564 경비원/input.txt", "r")

M, N = map(int, sys.stdin.readline().rstrip().split())
store = int(sys.stdin.readline().rstrip())
store_position = [ tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(store)]
player_position = tuple(map(int,sys.stdin.readline().rstrip().split()))

def dis(data):
    if data[0] == 1:
        return data[1]
    if data[0] == 4:
        return M + data[1]
    if data[0] == 2:
        return M+M+N-data[1]
    if data[0] == 3:
        return 2*(M + N) - data[1]
    

def solution(data):
    store_dis = dis(data)
    first_way = abs(store_dis - player_dis)
    second_way = 2*(M+N) - first_way
    return min(first_way, second_way)


player_dis = dis(player_position)
result = 0
for store in store_position:
    result += solution(store)

print(result)
