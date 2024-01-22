import sys
sys.stdin = open("data.txt", "r")


T = int(input())

case_list = []
result_list = []
stack = []
pointer = 0

for _ in range(T):
  case_list.append(int(input()))

for num in range(1,T + 1):
  stack.append(num)
  result_list.append('+')
  while num == case_list[pointer]:
    stack.pop()
    result_list.append('-')
    pointer += 1
    if len(stack) >= 1: 
      num = stack[-1]
    else:
      break
if pointer != T :
  print("NO")
else:
  for item in result_list:
    print(item)