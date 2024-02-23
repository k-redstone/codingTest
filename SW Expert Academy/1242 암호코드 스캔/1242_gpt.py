import sys
sys.stdin = open("./input.txt", "r")
T = int(input())

hex_to_bin = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}

codes = {
    '3211': 0,
    '2221': 1,
    '2122': 2,
    '1411': 3,
    '1132': 4,
    '1231': 5,
    '1114': 6,
    '1312': 7,
    '1213': 8,
    '3112': 9,
}

def change_final(code, num):
    r = 7 * num
    result_list = []
    for idx in range(0, len(code), r):
        result = code[idx:idx+r]
        result_list.append(codes[get_bin(result, num)])
    return result_list

def get_bin(code, num):
    temp = 1
    result = ''
    for idx in range(len(code)):
        if idx == len(code) - 1:
            if code[idx] == code[idx - 1]:
                result += str(temp // num)
                break
            if code[idx] != code[idx - 1]:
                result += '1'
                break
        if code[idx] == code[idx + 1]:
            temp += 1
        else:
            result += str(temp // num)
            temp = 1
    return result

def trans_bin(case):
    global cnt
    basic = 7
    idx = len(case)
    while idx >= 0:
        if case[idx - 1] == '1':
            while True:
                code_length = get_bin(case[idx - basic:idx], basic // 7)
                if codes.get(code_length) is not None:
                    code_length = basic // 7
                    break
                basic += 7
            judge_code = case[idx - (code_length*56):idx]
            final_num = change_final(judge_code, code_length)
            judge(final_num)
            idx = idx - (code_length*56)
            continue
        idx -= 1


def judge(item):
    global cnt
    temp_even = 0
    temp_odd = 0
    for idx, num in enumerate(item):
        if idx != 7:
            if idx % 2 == 1:
                temp_even += num
            else:
                temp_odd += num
    code = temp_odd * 3 + temp_even + item[7]
    cnt += sum(item) if code % 10 == 0 else 0

for tc in range(1, T+1):
    N, M = map(int, input().strip().split())
    case_matrix = set()
    for _ in range(N):
        case_matrix.add(input().strip())
    case_matrix = list(case_matrix)

    cnt = 0
    for idx in range(len(case_matrix)):
        for k, v in hex_to_bin.items():
            case_matrix[idx] = case_matrix[idx].replace(k, v)
        if '1' in case_matrix[idx]:
            trans_bin(case_matrix[idx])
    print(f'#{tc} {cnt}')