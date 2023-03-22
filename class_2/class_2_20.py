import sys

input = sys.stdin.readline

# 다른 사람의 코드

n = int(input())
q = []
stack = []
result = []
i = 1

for j in range(n):
    x = int(input())
    q.append(x)


for k in q:
    while i <= k:
        stack.append(i)
        result.append("+")
        i += 1
    if stack[-1] == k:
        result.append("-")
        stack.pop()
    else:
        print("NO")
        break
else:
    print("\n".join(result))


# 나의 코드

# n = int(input())
# q = []
# stack = []
# result = []
# i = 1

# for j in range(n):
#     x = int(input())
#     q.append(x)


# for k in q:
#     if k >= i:
#         for j in range(i, k + 1):
#             result.append("+")
#             stack.append(i)
#             i += 1
#         result.append("-")
#         stack.pop()
#     else:
#         if k in stack:
#             while True:
#                 pop_value = stack.pop()
#                 result.append("-")
#                 if pop_value == k:
#                     break
#         else:
#             print("NO")
#             break
# else:
#     for i in result:
#         print(i) 