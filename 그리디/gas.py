# import sys

# input = sys.stdin.readline

# n = int(input())

# length = list(map(int, input().split()))
# city = list(map(int, input().split()))

# flag = False
# result = 0
# temp = 0
# tempI = 0
# i = 0
# isMax = False
# while True:
#     if flag == False:
#         if city[i] > city[i + 1]:
#             result += city[i] * length[i]
#         else:
#             temp = city[i]
#             tempI = i
#             flag = True
#     else:
#         if temp > city[i] or i == len(city) - 2:
#             for j in range(tempI, i):
#                 result += temp * length[j]
#             if temp > city[i]:
#                 flag = False
#                 temp = 0
#                 tempI = 0
#                 i -= 1
#             else:
#                 flag = False
#             if i == len(city) - 2:
#                 isMax = True
#     i += 1
#     if i == len(city) - 1:
#         break
# if isMax == True:
#     result += temp * length[len(length) - 1]
# print(result)

import sys

input = sys.stdin.readline

n = int(input())

length = list(map(int, input().split()))
city = list(map(int, input().split()))

result = 0
min = city[0]

for i in range(len(city) - 1):
    if city[i] < min:
        min = city[i]
    result += min * length[i]
print(result)