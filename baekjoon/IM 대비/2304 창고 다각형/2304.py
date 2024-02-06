import sys
sys.stdin = open("./baekjoon/IM 대비/2304 창고 다각형/input.txt", "r")

count = int(sys.stdin.readline())
build_list = []
for _ in range(count):
    build_list.append(tuple(map(int, sys.stdin.readline().split())))
build_list = sorted(build_list, key= lambda item: item[0])


def buiild(info_list):
    stack = []
    max_h = 0
    for idx, item in enumerate(info_list):
        # 첫번째 요소로 지정
        if max_h == 0:
            # 최대 높이, 넓이 설정
            max_h = item[1]
            max_w = item[0]
            continue
        # 현재 요소의 높이가 최대높이보다 크거나 같을때
        if item[1] >= max_h:
            # 현재 넓이에서 최대 넓이를 뺸 값 만큼 최대 높이를 넣어줌
            for _ in range(item[0] - max_w):
                stack.append(max_h)
            # 최대 높이,넓이 다시 설정
            max_h = item[1]
            max_w = item[0]
        # 현재 요소의 높이가 최대높이보다 작을 때
        else:
            # 현재 요소에서 배열의 끝까지 높이가 가장 큰 값을 찾음
            max_point = max(info_list[idx:], key= lambda item: item[1])
            # 최대 높이가 위에서 찾은 높이보다 작거나 같다면
            if max_h <= max_point[1]:
                # 현재 넓이에서 최대 넓이를 뺸 값 만큼 최대 높이를 넣어줌
                for _ in range(item[0] - max_w):
                    stack.append(max_h)
                # 최대 넓이 설정
                max_w = item[0]
            # 최대 높이가 위에서 찾은 높이보다 크면
            else:
                # 최대 높이를 한번 넣어주고
                stack.append(max_h)
                # 현재 넓이 - 최대 넓이 -1 값 만큼 찾은 최대높이를 더해줌
                for _ in range(item[0] - max_w - 1):
                    stack.append(max_point[1])
                # 최대 높이를 찾은 높이 값으로 최대 넓이를 현재의 넓이로 설정
                max_h = max_point[1]
                max_w = item[0]
    return stack

# 위에 함수에서 구한 리스트의 합에서 정렬된 기둥의 높이 중 마지막을 더해준다
# why? 위 함수는 자기 요소 기준 그 뒤에까지의 합을 구해준거임
print(sum(buiild(build_list)) + build_list[-1][1])