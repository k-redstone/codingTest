import sys
# sys.stdin = open("data.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())

password_dic = {}

for _ in range(N):
    site, password = input().rstrip().split()
    password_dic[site] = password

# print(password_dic)

for _ in range(M):
    site = input().rstrip()
    print(password_dic[site])