import sys
sys.stdin = open('./input.txt', 'r')

en_to_num = {
    'ZRO': 0,
    'ONE': 1,
    'TWO': 2,
    'THR': 3,
    'FOR': 4,
    'FIV': 5,
    'SIX': 6,
    'SVN': 7,
    'EGT': 8,
    'NIN': 9
}
num_to_en = {
    0: 'ZRO',
    1: 'ONE',
    2: 'TWO',
    3: 'THR',
    4: 'FOR',
    5: 'FIV',
    6: 'SIX',
    7: 'SVN',
    8: 'EGT',
    9: 'NIN'
}
T = int(input())

for tc in range(1, T + 1):
    case_num, case_len = input().split()
    case_list = input().split()
    sorted_list = []
    for item in case_list:
        sorted_list.append(en_to_num[item])
    sorted_list = sorted(sorted_list)

    print(f'#{tc}')
    for item in sorted_list:
        print(num_to_en[item], end=" ")
    print()

