import sys
sys.stdin = open("data.txt", "r")


N, K = list(map(int,input().split()))

round_table = list(range(1, N +1))
num = 0
result_list = []

while len(round_table) > 0:
  if num <= len(round_table):
    num += K
    if num > len(round_table):
      while num > len(round_table):
        num -= len(round_table)
  result_list.append(round_table.pop(num - 1))
  num -= 1

print(f'<{", ".join(map(str,result_list))}>')