
# import sys

# n = int(sys.stdin.readline().rstrip())
# result = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

# def solution(n, result):
#     answer = []
#     stack = []
#     current = 1

#     for num in result:
#         while current <= num:  # 현재 수가 수열의 수보다 작거나 같으면 push
#             stack.append(current)
#             answer.append('+')
#             current += 1
#         if stack[-1] == num:  # 스택의 마지막 수가 수열의 수와 같으면 pop
#             stack.pop()
#             answer.append('-')
#         else:  # 만약 수열을 만들 수 없는 경우
#             print('NO')
#             return

#     print('\n'.join(answer))

# solution(n, result)