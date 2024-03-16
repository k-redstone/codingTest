import sys
from itertools import combinations
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def solution():
    start_num = min(len(A), len(B))
    A_dict = dict()
    while start_num >= 1:
        for item in combinations(A, start_num):
            A_dict[item] = 1
        for b in combinations(B, start_num):
            if A_dict.get(b) is not None:
                print(start_num)
                print(''.join(item))
                return
        else:
            start_num -= 1
    print('0')

A = input().rstrip()
B = input().rstrip()

solution()