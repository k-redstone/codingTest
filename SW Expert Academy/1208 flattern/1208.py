import sys
sys.stdin = open("input.txt", "r")

T = 10

for _ in range(T):
    # input 값 할당
    N = int(input().rstrip())
    case_list = list(map(int, input().rstrip().split()))

    # 가로 길이는 항상 100으로 고정되어 주어짐
    box_area = [0] * 101
    max_pointer = 100
    min_pointer = 0

    # 주어진 박스길이를 카운팅
    for x in range(len(box_area) - 1):
        box_area[case_list[x]] += 1

    # 정해진 덤프만큼 반복하면서
    # max_pointer 에서 1빼고, max_pointer + 1 은 1 더하기
    # min_pointer 에서 1빼고, min_pointer + 1 은 1 더하기
    for i in range(N + 1):
        while box_area[max_pointer] == 0:
            max_pointer -= 1
        while box_area[min_pointer] == 0:
            min_pointer += 1
        if max_pointer == min_pointer:
            break
        # if i == N:
        #     print("끝")
        box_area[max_pointer] -= 1
        box_area[max_pointer - 1] += 1
        box_area[min_pointer + 1] += 1
        box_area[min_pointer] -= 1

    print(f'#{_ + 1} {max_pointer - min_pointer}')
