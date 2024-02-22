import sys
sys.stdin = open("./input.txt", "r")

T = int(input())

codes = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}



def scan(item):
    for idx in range(M-1, -1, -1):
        if item[idx] == '1':
            return item[idx - 55:idx + 1]
    return False

def trans(item):
    return_code = []
    for idx in range(55, -1, -7):
        temp = item[idx-6:idx+1]
        return_code.append(codes[temp])
    return return_code

def judge(item):
    temp_even = 0
    temp_odd = 0
    for idx, num in enumerate(item):
        if idx % 2 == 1:
            temp_odd += num
        else:
            temp_even += num

    code = temp_odd*3 + temp_even
    if code % 10 == 0:
        return sum(item)
    else:
        return 0

for tc in range(1, T+1):
    N, M = map(int, input().split())
    case_matrix = [input() for _ in range(N)]

    for case in case_matrix:
        scan_list = scan(case)
        if scan_list:
            break
    print(f'#{tc} {judge(trans(scan_list))}')