import sys
sys.stdin = open("data.txt", "r")


T = int(sys.stdin.readline().rstrip())
case_list = [int(sys.stdin.readline().rstrip()) for _ in range(T)]


def solution():
  result_list = []
  stack = []
  pointer = 1

  for num in case_list:
    while pointer <= num:
      stack.append(pointer)
      result_list.append('+')
      pointer += 1

    if stack[-1] == num:
      stack.pop()
      result_list.append('-')
    else:
      print("NO")
      return
  print('\n'.join(result_list))

solution()