import sys
sys.stdin = open("./baekjoon/2493 탑/input.txt", "r")

N = int(sys.stdin.readline().rstrip())
case_list = list(map(int, sys.stdin.readline().rstrip().split()))

stack = [(case_list[0], 1)]
cur = 1
result = [0]
for num in range(1, N):
    if stack[-1][0] < case_list[num]:
        while stack:
            stack.pop()
            if stack and stack[-1][0] > case_list[num]:
                result.append(stack[-1][1])
                stack.append((case_list[num], num+1))
                cur = stack[-1][1]
                break
            if not stack:
                stack.append((case_list[num], num+1))
                result.append(0)
                cur = stack[-1][1]
                break
    else:
        stack.append((case_list[num], num+1))
        result.append(cur)
        cur = stack[-1][1]
print(*result)