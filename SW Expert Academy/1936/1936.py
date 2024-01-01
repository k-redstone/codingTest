import sys
sys.stdin = open("./SW Expert Academy/input.txt", "r")

a,b = map(int, input().split())

def judge(a,b):
  if abs((a-b)) == 1:
    if a > b:
      print("A")
    else:
      print("B")

  elif abs((a-b)) == 2:
    if a > b:
      print("B")
    else:
      print("A")


judge(a,b)