import sys
from collections import deque
sys.stdin = open("./baekjoon/class.3/5430 AC/input.txt", "r")

T = int(sys.stdin.readline())


def solution(func_list, deq, length):
    direction = 0
    for func in func_list:
        if func == 'R':
            direction = not direction
            continue
        if func == 'D':
            if length == 0:
                return False
            if direction == 0:
                deq.popleft()
                length -= 1
            if direction == 1:
                deq.pop()
                length -= 1
    if direction == 1:
        return reversed(deq)
    return deq


for _ in range(T):
    func_list = list(sys.stdin.readline().rstrip())
    list_length = int(sys.stdin.readline())
    dp = deque(sys.stdin.readline().rstrip()[1:-1].split(','))
    result = solution(func_list, dp, list_length)
    if result is False:
        print('error')
    else:
        print('[' + ','.join(result) +']')