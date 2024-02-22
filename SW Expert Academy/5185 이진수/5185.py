import sys
sys.stdin = open("./input.txt", "r")

T = int(input())

trans = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
}

def solution(num):
    return bin(num)[2:].zfill(4)


for tc in range(1, T+1):
    N, num = input().split()
    result = ''
    for item in num:
        if item.isnumeric():
            result += solution(int(item))
        else:
            result += solution(trans[item])
    print(f'#{tc} {result}')