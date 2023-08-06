# import sys

# input = sys.stdin.readline

# N = int(input())

# x_i = list(map(int, input().split()))

# x_i_sort = sorted(list(set(x_i)))

# # 여기서 그냥 배열끼리 비교해서
# # 하면 index 시간 복잡도가 O(n)이라서 n^2이 된다
# # 이 문제 n이 100만까지이므로 100만 X 100만이 되어버림
# # for i in x_i:
#     # print(x_i_sort.index(i), end=" ")

# # 튜플로 만들면 찾는 시간 복잡도가
# # O(1)이므로 시간이 많이 줄어든다.
# dic = {x_i_sort[i] : i for i in range(len(x_i_sort))}
# for i in x_i:
#     print(dic[i], end=" ")

# items = ['1', '2', '3', '4']
# from itertools import permutations
# print(list(permutations(items, 4)))

# import sys
# input = sys.stdin.readline

# T = int(input())

# for _ in range(T):
#     n, d = map(int, input().split())
#     lst = []
#     for _ in range(n):
#         lst.append(list(map(int, input().split())))
    
#     if d < 0:
#         d = 360 + d
        

#     new_lst = [[0 for _ in range(n)] for _ in range(n)]
    
#     while d > 0:
#         x, y = n // 2 - 1, n // 2 - 1
#         i = 3
#         plus = 1
#         while i <= n:
#             for k in range(8):
#                 num = lst[x][y]
#                 # y 2번 증가
#                 if k >= 0 and k < 2:
#                     y += plus
#                 # x 2번 증가
#                 elif k >= 2 and k < 4:
#                     x += plus
#                 # y 2번 감소
#                 elif k >= 4 and k < 6:
#                     y -= plus
#                 # x 2번 감소
#                 elif k >= 6 and k < 8:
#                     x -= plus
#                 new_lst[x][y] = num
#             x -= 1
#             y -= 1
#             plus += 1
#             i += 2
#         for a in range(len(lst)):
#             for b in range(len(lst[a])):
#                 if new_lst[a][b] == 0:
#                     new_lst[a][b] = lst[a][b]
#         lst = new_lst
#         new_lst = [[0 for _ in range(n)] for _ in range(n)]
#         d -= 45

#     for a in range(len(lst)):
#             for b in range(len(lst[a])):
#                 print(lst[a][b], end = " ")
#             print()

import sys
import itertools

def input():
    return sys.stdin.readline()

n, m = map(int, input().split())

data = []
chicken = []
city = []

for _ in range(n):
    data.append(list(map(int, input().split())))

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == 1:
            city.append([i, j])
        elif data[i][j] == 2:
            chicken.append([i, j])

chicken_comb = list(itertools.combinations(chicken, m))

result = 10000

for ch_cm in chicken_comb:
    city_dist = 0
    for c in city:
        dist = 10000
        for ch in ch_cm:
            dist = min(dist, abs(c[0] - ch[0]) + abs(c[1] - ch[1]))
        city_dist += dist
    result = min(result, city_dist)

print(result)
        
