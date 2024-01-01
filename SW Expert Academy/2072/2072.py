import sys
sys.stdin = open("./SW Expert Academy/input.txt", "r")

listCount = int(input())

num = 1
for numList in range(listCount):
  lists = list(filter(lambda num: num % 2 == 1, sorted(list(map(int, input().split())))))
  print(f'#{num} {sum(lists)}')
  num +=1