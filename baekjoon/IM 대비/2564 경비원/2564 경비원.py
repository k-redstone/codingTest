import sys
sys.stdin = open("data.txt", "r")

M, N = map(int, sys.stdin.readline().rstrip().split())
store = int(sys.stdin.readline().rstrip())
store_position = [ tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(store)]
player_position = tuple(map(int,sys.stdin.readline().rstrip().split()))
# 4 -> 동
# 3 -> 서
# 2 -> 남
# 1 -> 북

def convert(data):
    if data[0] == 4:
        return (M, data[1])
    if data[0] == 3:
        return (0, data[1])
    if data[0] == 2:
        return (data[1], N)
    if data[0] == 1:
        return (data[1], 0)


convert_list = []
for postion in store_position:
    convert_list.append(convert(postion))
player_position = convert(player_position)

print(convert_list)
print(player_position)
# for item in convert_list:
