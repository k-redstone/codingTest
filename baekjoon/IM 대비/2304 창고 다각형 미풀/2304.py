import sys
sys.stdin = open("./baekjoon/IM 대비/2304 창고 다각형/input.txt", "r")

count = int(sys.stdin.readline())
build_list = []
print('전체 갯수 ', count)
for _ in range(count):
    build_list.append(tuple(map(int, sys.stdin.readline().split())))

build_list = sorted(build_list, key= lambda item: item[0])

print( build_list)
# def buiild(info_list):
#     stack = []
#     max_h = 0

#     for idx, item in enumerate(info_list):
#         if max_h == 0:
#             max_h = item[1]
#             stack.append(item[1])
#             continue
#         else:
#             if item[1] >= max_h:
        

#     return stack

# print(buiild(build_list))