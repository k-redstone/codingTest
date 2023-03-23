# https://www.acmicpc.net/problem/10812

import sys
sys.stdin = open("data.txt", "r")
input = sys.stdin.readline


n, m = map(int, input().split())
list = [i+1 for i in range(n)]
for _ in range(m):
    i, j, k = map(int, input().split())
    list = list[:i-1] + list[k-1:j] + list[i-1:k-1] + list[j:]
for i in list:
    print(i, end=" ")
